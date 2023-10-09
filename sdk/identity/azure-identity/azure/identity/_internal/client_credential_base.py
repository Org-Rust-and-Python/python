# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
import time
from typing import Any, Optional, Dict

from azure.core.credentials import AccessToken
from azure.core.exceptions import ClientAuthenticationError
from .get_token_mixin import GetTokenMixin

from . import wrap_exceptions
from .msal_credentials import MsalCredential


def _get_known_kwargs(kwargs: Dict[str, Any]):
    # Remove kwargs not expected by MSAL. These aren't typically passed by users, but this is a precaution.
    known_kwargs = {"force_refresh", "authority", "correlation_id", "data"}
    return {k: v for k, v in kwargs.items() if k in known_kwargs}


class ClientCredentialBase(MsalCredential, GetTokenMixin):
    """Base class for credentials authenticating a service principal with a certificate or secret"""

    @wrap_exceptions
    def _acquire_token_silently(self, *scopes: str, **kwargs: Any) -> Optional[AccessToken]:
        app = self._get_app(**kwargs)
        request_time = int(time.time())
        result = app.acquire_token_silent_with_error(
            list(scopes), account=None, claims_challenge=kwargs.pop("claims", None), **_get_known_kwargs(kwargs)
        )
        if result and "access_token" in result and "expires_in" in result:
            return AccessToken(result["access_token"], request_time + int(result["expires_in"]))
        return None

    @wrap_exceptions
    def _request_token(self, *scopes: str, **kwargs: Any) -> Optional[AccessToken]:
        app = self._get_app(**kwargs)
        request_time = int(time.time())
        result = app.acquire_token_for_client(list(scopes), claims_challenge=kwargs.pop("claims", None))
        if "access_token" not in result:
            message = "Authentication failed: {}".format(result.get("error_description") or result.get("error"))
            raise ClientAuthenticationError(message=message)

        return AccessToken(result["access_token"], request_time + int(result["expires_in"]))
