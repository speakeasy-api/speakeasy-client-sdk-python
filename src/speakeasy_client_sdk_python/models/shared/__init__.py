"""Code generated by Speakeasy (https://speakeasy.com). DO NOT EDIT."""

from .accessdetails import AccessDetails, AccessDetailsTypedDict, Level
from .accesstoken import AccessToken, AccessTokenTypedDict, AccessTokenUser, AccessTokenUserTypedDict, Claims, ClaimsTypedDict, Workspaces, WorkspacesTypedDict
from .accounttype import AccountType
from .addtags import AddTags, AddTagsTypedDict
from .annotations import Annotations, AnnotationsTypedDict
from .api import API, APITypedDict
from .api_input import APIInput, APIInputTypedDict
from .apiendpoint import APIEndpoint, APIEndpointTypedDict
from .apiendpoint_input import APIEndpointInput, APIEndpointInputTypedDict
from .apikeydetails import APIKeyDetails, APIKeyDetailsTypedDict
from .boundedrequest import BoundedRequest, BoundedRequestTypedDict
from .clievent import CliEvent, CliEventTypedDict, GenerateBumpType, OpenapiDiffBumpType
from .embedaccesstokenresponse import EmbedAccessTokenResponse, EmbedAccessTokenResponseTypedDict
from .embedtoken import EmbedToken, EmbedTokenTypedDict
from .featureflag import FeatureFlag, FeatureFlagTypedDict
from .filter_ import Filter, FilterTypedDict
from .filters import Filters, FiltersTypedDict
from .generateopenapispecdiff import GenerateOpenAPISpecDiff, GenerateOpenAPISpecDiffTypedDict
from .getnamespacesresponse import GetNamespacesResponse, GetNamespacesResponseTypedDict
from .getrevisionsresponse import GetRevisionsResponse, GetRevisionsResponseTypedDict
from .gettagsresponse import GetTagsResponse, GetTagsResponseTypedDict
from .githubconfigurecodesamplesrequest import GithubConfigureCodeSamplesRequest, GithubConfigureCodeSamplesRequestTypedDict
from .githubconfigurecodesamplesresponse import GithubConfigureCodeSamplesResponse, GithubConfigureCodeSamplesResponseTypedDict
from .githubconfiguremintlifyreporequest import GithubConfigureMintlifyRepoRequest, GithubConfigureMintlifyRepoRequestTypedDict
from .githubconfiguretargetrequest import GithubConfigureTargetRequest, GithubConfigureTargetRequestTypedDict
from .githubgetactionresponse import GithubGetActionResponse, GithubGetActionResponseTypedDict
from .githubmissingpublishingsecretsresponse import GithubMissingPublishingSecretsResponse, GithubMissingPublishingSecretsResponseTypedDict
from .githubpublishingprresponse import GithubPublishingPRResponse, GithubPublishingPRResponseTypedDict
from .githubstorepublishingsecretsrequest import GithubStorePublishingSecretsRequest, GithubStorePublishingSecretsRequestTypedDict
from .githubtriggeractionrequest import GithubTriggerActionRequest, GithubTriggerActionRequestTypedDict
from .interactiontype import InteractionType
from .manifest import Manifest, ManifestTypedDict
from .namespace import Namespace, NamespaceTypedDict
from .oasinfo import License, LicenseTypedDict, OASInfo, OASInfoTypedDict
from .oasoperation import OASOperation, OASOperationTypedDict
from .oassummary import OASSummary, OASSummaryTypedDict
from .organization import Organization, OrganizationTypedDict
from .organizationusage import OrganizationUsage, OrganizationUsageTypedDict
from .organizationusageresponse import OrganizationUsageResponse, OrganizationUsageResponseTypedDict
from .preflightrequest import PreflightRequest, PreflightRequestTypedDict
from .preflighttoken import PreflightToken, PreflightTokenTypedDict
from .report import Report, ReportTypedDict, Type
from .requestmetadata import RequestMetadata, RequestMetadataTypedDict
from .revision import Revision, RevisionTypedDict
from .schema import Schema, SchemaTypedDict
from .schemadiff import SchemaDiff, SchemaDiffTypedDict, ValueChange, ValueChangeTypedDict
from .security import Security, SecurityTypedDict
from .shorturl import ShortURL, ShortURLTypedDict
from .suggestedoperationids import SuggestedOperationIDs, SuggestedOperationIDsTypedDict
from .suggestoperationidsopts import DepthStyle, Style, SuggestOperationIDsOpts, SuggestOperationIDsOptsTypedDict
from .tag import Tag, TagTypedDict
from .targetsdk import TargetSDK, TargetSDKTypedDict
from .unboundedrequest import UnboundedRequest, UnboundedRequestTypedDict
from .user import User, UserTypedDict
from .v2descriptor import V2Descriptor, V2DescriptorTypedDict
from .versionmetadata import VersionMetadata, VersionMetadataTypedDict
from .versionmetadata_input import VersionMetadataInput, VersionMetadataInputTypedDict
from .workflowdocument import Auth, AuthTypedDict, WorkflowDocument, WorkflowDocumentTypedDict
from .workspace import Workspace, WorkspaceTypedDict

__all__ = ["API", "APIEndpoint", "APIEndpointInput", "APIEndpointInputTypedDict", "APIEndpointTypedDict", "APIInput", "APIInputTypedDict", "APIKeyDetails", "APIKeyDetailsTypedDict", "APITypedDict", "AccessDetails", "AccessDetailsTypedDict", "AccessToken", "AccessTokenTypedDict", "AccessTokenUser", "AccessTokenUserTypedDict", "AccountType", "AddTags", "AddTagsTypedDict", "Annotations", "AnnotationsTypedDict", "Auth", "AuthTypedDict", "BoundedRequest", "BoundedRequestTypedDict", "Claims", "ClaimsTypedDict", "CliEvent", "CliEventTypedDict", "DepthStyle", "EmbedAccessTokenResponse", "EmbedAccessTokenResponseTypedDict", "EmbedToken", "EmbedTokenTypedDict", "FeatureFlag", "FeatureFlagTypedDict", "Filter", "FilterTypedDict", "Filters", "FiltersTypedDict", "GenerateBumpType", "GenerateOpenAPISpecDiff", "GenerateOpenAPISpecDiffTypedDict", "GetNamespacesResponse", "GetNamespacesResponseTypedDict", "GetRevisionsResponse", "GetRevisionsResponseTypedDict", "GetTagsResponse", "GetTagsResponseTypedDict", "GithubConfigureCodeSamplesRequest", "GithubConfigureCodeSamplesRequestTypedDict", "GithubConfigureCodeSamplesResponse", "GithubConfigureCodeSamplesResponseTypedDict", "GithubConfigureMintlifyRepoRequest", "GithubConfigureMintlifyRepoRequestTypedDict", "GithubConfigureTargetRequest", "GithubConfigureTargetRequestTypedDict", "GithubGetActionResponse", "GithubGetActionResponseTypedDict", "GithubMissingPublishingSecretsResponse", "GithubMissingPublishingSecretsResponseTypedDict", "GithubPublishingPRResponse", "GithubPublishingPRResponseTypedDict", "GithubStorePublishingSecretsRequest", "GithubStorePublishingSecretsRequestTypedDict", "GithubTriggerActionRequest", "GithubTriggerActionRequestTypedDict", "InteractionType", "Level", "License", "LicenseTypedDict", "Manifest", "ManifestTypedDict", "Namespace", "NamespaceTypedDict", "OASInfo", "OASInfoTypedDict", "OASOperation", "OASOperationTypedDict", "OASSummary", "OASSummaryTypedDict", "OpenapiDiffBumpType", "Organization", "OrganizationTypedDict", "OrganizationUsage", "OrganizationUsageResponse", "OrganizationUsageResponseTypedDict", "OrganizationUsageTypedDict", "PreflightRequest", "PreflightRequestTypedDict", "PreflightToken", "PreflightTokenTypedDict", "Report", "ReportTypedDict", "RequestMetadata", "RequestMetadataTypedDict", "Revision", "RevisionTypedDict", "Schema", "SchemaDiff", "SchemaDiffTypedDict", "SchemaTypedDict", "Security", "SecurityTypedDict", "ShortURL", "ShortURLTypedDict", "Style", "SuggestOperationIDsOpts", "SuggestOperationIDsOptsTypedDict", "SuggestedOperationIDs", "SuggestedOperationIDsTypedDict", "Tag", "TagTypedDict", "TargetSDK", "TargetSDKTypedDict", "Type", "UnboundedRequest", "UnboundedRequestTypedDict", "User", "UserTypedDict", "V2Descriptor", "V2DescriptorTypedDict", "ValueChange", "ValueChangeTypedDict", "VersionMetadata", "VersionMetadataInput", "VersionMetadataInputTypedDict", "VersionMetadataTypedDict", "WorkflowDocument", "WorkflowDocumentTypedDict", "Workspace", "WorkspaceTypedDict", "Workspaces", "WorkspacesTypedDict"]