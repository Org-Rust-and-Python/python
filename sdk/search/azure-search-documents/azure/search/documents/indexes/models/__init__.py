# --------------------------------------------------------------------------
#
# Copyright (c) Microsoft Corporation. All rights reserved.
#
# The MIT License (MIT)
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the ""Software""), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED *AS IS*, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.
#
# --------------------------------------------------------------------------

from ._index import (
    ComplexField,
    SearchField,
    SearchableField,
    SimpleField,
    SearchIndex,
)
from . import _edm
from ..._generated.models import SuggestOptions
from .._generated.models import (
    SearchAlias,
    AzureMachineLearningSkill,
    AnalyzeResult,
    AnalyzedTokenInfo,
    AsciiFoldingTokenFilter,
    AzureOpenAIEmbeddingSkill,
    AzureOpenAIParameters,
    AzureOpenAIVectorizer,
    BlobIndexerDataToExtract,
    BlobIndexerImageAction,
    BlobIndexerParsingMode,
    BlobIndexerPDFTextRotationAlgorithm,
    BM25Similarity,
    CharFilter,
    CharFilterName,
    CjkBigramTokenFilter,
    ClassicSimilarity,
    ClassicTokenizer,
    CognitiveServicesAccount,
    CognitiveServicesAccountKey,
    CommonGramTokenFilter,
    ConditionalSkill,
    CorsOptions,
    CustomEntity,
    CustomEntityAlias,
    CustomEntityLookupSkill,
    CustomVectorizer,
    CustomWebApiParameters,
    CustomEntityLookupSkillLanguage,
    CustomNormalizer,
    DataChangeDetectionPolicy,
    DataDeletionDetectionPolicy,
    DefaultCognitiveServicesAccount,
    DictionaryDecompounderTokenFilter,
    DistanceScoringFunction,
    DistanceScoringParameters,
    DocumentExtractionSkill,
    DocumentKeysOrIds,
    EdgeNGramTokenFilter,
    EdgeNGramTokenizer,
    EdgeNGramTokenFilterSide,
    ElisionTokenFilter,
    EntityCategory,
    EntityLinkingSkill,
    EntityRecognitionSkillLanguage,
    ExhaustiveKnnAlgorithmConfiguration,
    ExhaustiveKnnParameters,
    FieldMapping,
    FieldMappingFunction,
    FreshnessScoringFunction,
    FreshnessScoringParameters,
    GetIndexStatisticsResult,
    HighWaterMarkChangeDetectionPolicy,
    HnswParameters,
    HnswAlgorithmConfiguration,
    ImageAnalysisSkill,
    ImageAnalysisSkillLanguage,
    ImageDetail,
    IndexerExecutionResult,
    IndexerExecutionStatus,
    IndexProjectionMode,
    IndexerStatus,
    IndexingParameters,
    IndexingParametersConfiguration,
    IndexingSchedule,
    InputFieldMappingEntry,
    KeepTokenFilter,
    KeyPhraseExtractionSkill,
    KeyPhraseExtractionSkillLanguage,
    KeywordMarkerTokenFilter,
    KeywordTokenizerV2,
    LanguageDetectionSkill,
    LengthTokenFilter,
    LexicalAnalyzer,
    LexicalNormalizer,
    LexicalNormalizerName,
    LexicalAnalyzerName,
    LexicalTokenizer,
    LexicalTokenizerName,
    LimitTokenFilter,
    LuceneStandardAnalyzer,
    LuceneStandardTokenizer,
    MagnitudeScoringFunction,
    MagnitudeScoringParameters,
    MappingCharFilter,
    MergeSkill,
    MicrosoftLanguageStemmingTokenizer,
    MicrosoftLanguageTokenizer,
    MicrosoftStemmingTokenizerLanguage,
    MicrosoftTokenizerLanguage,
    NGramTokenFilter,
    NGramTokenizer,
    OcrSkill,
    OcrSkillLanguage,
    OutputFieldMappingEntry,
    PathHierarchyTokenizerV2,
    PatternCaptureTokenFilter,
    PatternReplaceCharFilter,
    PatternReplaceTokenFilter,
    PhoneticEncoder,
    PhoneticTokenFilter,
    PIIDetectionSkill,
    PIIDetectionSkillMaskingMode,
    RegexFlags,
    ScoringFunction,
    ScoringFunctionAggregation,
    ScoringFunctionInterpolation,
    ScoringProfile,
    SearchIndexer,
    SearchIndexerCache,
    SearchIndexerDataContainer,
    SearchIndexerDataIdentity,
    SearchIndexerDataNoneIdentity,
    SearchIndexerDataUserAssignedIdentity,
    SearchIndexerDataSourceType,
    SearchIndexerError,
    SearchIndexerIndexProjections,
    SearchIndexerIndexProjectionSelector,
    SearchIndexerIndexProjectionsParameters,
    SearchIndexerKnowledgeStore,
    SearchIndexerKnowledgeStoreBlobProjectionSelector,
    SearchIndexerKnowledgeStoreFileProjectionSelector,
    SearchIndexerKnowledgeStoreObjectProjectionSelector,
    SearchIndexerKnowledgeStoreProjection,
    SearchIndexerKnowledgeStoreProjectionSelector,
    SearchIndexerKnowledgeStoreTableProjectionSelector,
    SearchIndexerLimits,
    SearchIndexerSkill,
    SearchIndexerStatus,
    SearchIndexerWarning,
    SemanticConfiguration,
    SemanticField,
    SemanticPrioritizedFields,
    SemanticSearch,
    SemanticSettings,
    SentimentSkillLanguage,
    ShaperSkill,
    ShingleTokenFilter,
    Similarity,
    SnowballTokenFilter,
    SnowballTokenFilterLanguage,
    SoftDeleteColumnDeletionDetectionPolicy,
    SplitSkill,
    SplitSkillLanguage,
    SqlIntegratedChangeTrackingPolicy,
    StemmerOverrideTokenFilter,
    StemmerTokenFilter,
    StemmerTokenFilterLanguage,
    StopAnalyzer,
    StopwordsList,
    StopwordsTokenFilter,
    Suggester,
    SynonymTokenFilter,
    TagScoringFunction,
    TagScoringParameters,
    TextSplitMode,
    TextTranslationSkill,
    TextTranslationSkillLanguage,
    TextWeights,
    TokenCharacterKind,
    TokenFilter,
    TokenFilterName,
    TruncateTokenFilter,
    UaxUrlEmailTokenizer,
    UniqueTokenFilter,
    VectorSearch,
    VectorSearchAlgorithmConfiguration,
    VectorSearchAlgorithmKind,
    VectorSearchAlgorithmMetric,
    VectorSearchProfile,
    VectorSearchVectorizer,
    VectorSearchVectorizerKind,
    VisualFeature,
    WebApiSkill,
    WordDelimiterTokenFilter,
)
from ._models import (
    AnalyzeTextOptions,
    CustomAnalyzer,
    EntityRecognitionSkill,
    EntityRecognitionSkillVersion,
    PatternAnalyzer,
    PatternTokenizer,
    SearchIndexerDataSourceConnection,
    SearchIndexerSkillset,
    SearchResourceEncryptionKey,
    SentimentSkill,
    SentimentSkillVersion,
    SynonymMap,
)

SearchFieldDataType = _edm


class BM25SimilarityAlgorithm(BM25Similarity):
    pass


class ClassicSimilarityAlgorithm(ClassicSimilarity):
    pass


class KeywordTokenizer(KeywordTokenizerV2):
    pass


class PathHierarchyTokenizer(PathHierarchyTokenizerV2):
    pass


class SimilarityAlgorithm(Similarity):
    pass


class SearchSuggester(Suggester):
    pass


__all__ = (
    "SearchAlias",
    "AnalyzeTextOptions",
    "AnalyzeResult",
    "AnalyzedTokenInfo",
    "AsciiFoldingTokenFilter",
    "AzureOpenAIEmbeddingSkill",
    "AzureOpenAIParameters",
    "AzureOpenAIVectorizer",
    "AzureMachineLearningSkill",
    "BlobIndexerDataToExtract",
    "BlobIndexerImageAction",
    "BlobIndexerParsingMode",
    "BlobIndexerPDFTextRotationAlgorithm",
    "BM25SimilarityAlgorithm",
    "CharFilter",
    "CharFilterName",
    "CjkBigramTokenFilter",
    "ClassicSimilarityAlgorithm",
    "ClassicTokenizer",
    "CognitiveServicesAccount",
    "CognitiveServicesAccountKey",
    "CommonGramTokenFilter",
    "ComplexField",
    "ConditionalSkill",
    "CorsOptions",
    "CustomAnalyzer",
    "CustomEntity",
    "CustomEntityAlias",
    "CustomEntityLookupSkill",
    "CustomVectorizer",
    "CustomWebApiParameters",
    "DefaultCognitiveServicesAccount",
    "CustomEntityLookupSkillLanguage",
    "CustomNormalizer",
    "DataChangeDetectionPolicy",
    "DataDeletionDetectionPolicy",
    "DefaultCognitiveServicesAccount",
    "DictionaryDecompounderTokenFilter",
    "DistanceScoringFunction",
    "DistanceScoringParameters",
    "DocumentExtractionSkill",
    "DocumentKeysOrIds",
    "EdgeNGramTokenFilter",
    "EdgeNGramTokenizer",
    "ElisionTokenFilter",
    "EdgeNGramTokenFilterSide",
    "EntityCategory",
    "EntityLinkingSkill",
    "EntityRecognitionSkill",
    "EntityRecognitionSkillLanguage",
    "EntityRecognitionSkillVersion",
    "ExhaustiveKnnAlgorithmConfiguration",
    "ExhaustiveKnnParameters",
    "FieldMapping",
    "FieldMappingFunction",
    "FreshnessScoringFunction",
    "FreshnessScoringParameters",
    "GetIndexStatisticsResult",
    "HighWaterMarkChangeDetectionPolicy",
    "HnswParameters",
    "HnswAlgorithmConfiguration",
    "ImageAnalysisSkill",
    "ImageAnalysisSkillLanguage",
    "ImageDetail",
    "IndexingSchedule",
    "IndexingParameters",
    "IndexingParametersConfiguration",
    "IndexerExecutionResult",
    "IndexerExecutionStatus",
    "IndexProjectionMode",
    "IndexerStatus",
    "IndexingParameters",
    "IndexingParametersConfiguration",
    "IndexingSchedule",
    "InputFieldMappingEntry",
    "KeepTokenFilter",
    "KeyPhraseExtractionSkill",
    "KeyPhraseExtractionSkillLanguage",
    "KeywordMarkerTokenFilter",
    "KeywordTokenizer",
    "LanguageDetectionSkill",
    "LengthTokenFilter",
    "LexicalAnalyzer",
    "LexicalAnalyzerName",
    "LexicalNormalizer",
    "LexicalNormalizerName",
    "LexicalTokenizer",
    "LexicalTokenizerName",
    "LimitTokenFilter",
    "LuceneStandardAnalyzer",
    "LuceneStandardTokenizer",
    "MagnitudeScoringFunction",
    "MagnitudeScoringParameters",
    "MappingCharFilter",
    "MergeSkill",
    "MicrosoftLanguageStemmingTokenizer",
    "MicrosoftLanguageTokenizer",
    "MicrosoftStemmingTokenizerLanguage",
    "MicrosoftTokenizerLanguage",
    "NGramTokenFilter",
    "NGramTokenizer",
    "OcrSkill",
    "OcrSkillLanguage",
    "OutputFieldMappingEntry",
    "PathHierarchyTokenizer",
    "PatternAnalyzer",
    "PatternCaptureTokenFilter",
    "PatternReplaceCharFilter",
    "PatternReplaceTokenFilter",
    "PatternTokenizer",
    "PIIDetectionSkill",
    "PIIDetectionSkillMaskingMode",
    "PhoneticEncoder",
    "PhoneticTokenFilter",
    "RegexFlags",
    "ScoringFunction",
    "ScoringFunctionAggregation",
    "ScoringFunctionInterpolation",
    "ScoringProfile",
    "SearchField",
    "SearchIndex",
    "SearchIndexer",
    "SearchIndexerCache",
    "SearchIndexerDataContainer",
    "SearchIndexerDataIdentity",
    "SearchIndexerDataNoneIdentity",
    "SearchIndexerDataUserAssignedIdentity",
    "SearchIndexerDataSourceConnection",
    "SearchIndexerDataSourceType",
    "SearchIndexerError",
    "SearchIndexerIndexProjections",
    "SearchIndexerIndexProjectionSelector",
    "SearchIndexerIndexProjectionsParameters",
    "SearchIndexerKnowledgeStore",
    "SearchIndexerKnowledgeStoreBlobProjectionSelector",
    "SearchIndexerKnowledgeStoreFileProjectionSelector",
    "SearchIndexerKnowledgeStoreObjectProjectionSelector",
    "SearchIndexerKnowledgeStoreProjection",
    "SearchIndexerKnowledgeStoreProjectionSelector",
    "SearchIndexerKnowledgeStoreTableProjectionSelector",
    "SearchIndexerLimits",
    "SearchIndexerSkill",
    "SearchIndexerSkillset",
    "SearchIndexerStatus",
    "SearchIndexerWarning",
    "SearchResourceEncryptionKey",
    "SearchableField",
    "SemanticConfiguration",
    "SemanticField",
    "SemanticPrioritizedFields",
    "SemanticSearch",
    "SemanticSettings",
    "SentimentSkill",
    "SentimentSkillLanguage",
    "SentimentSkillVersion",
    "ShaperSkill",
    "ShingleTokenFilter",
    "SimpleField",
    "SimilarityAlgorithm",
    "SnowballTokenFilter",
    "SnowballTokenFilterLanguage",
    "SoftDeleteColumnDeletionDetectionPolicy",
    "SplitSkill",
    "SplitSkillLanguage",
    "SqlIntegratedChangeTrackingPolicy",
    "StemmerOverrideTokenFilter",
    "StemmerTokenFilter",
    "StemmerTokenFilterLanguage",
    "StopAnalyzer",
    "StopwordsList",
    "StopwordsTokenFilter",
    "SearchSuggester",
    "SuggestOptions",
    "SynonymMap",
    "SynonymTokenFilter",
    "TagScoringFunction",
    "TagScoringParameters",
    "TextSplitMode",
    "TextTranslationSkill",
    "TextTranslationSkillLanguage",
    "TextWeights",
    "TokenCharacterKind",
    "TokenFilter",
    "TokenFilterName",
    "TruncateTokenFilter",
    "UaxUrlEmailTokenizer",
    "UniqueTokenFilter",
    "VectorSearch",
    "VectorSearchAlgorithmConfiguration",
    "VectorSearchAlgorithmKind",
    "VectorSearchAlgorithmMetric",
    "VectorSearchProfile",
    "VectorSearchVectorizer",
    "VectorSearchVectorizerKind",
    "VisualFeature",
    "WebApiSkill",
    "WordDelimiterTokenFilter",
    "SearchFieldDataType",
)
