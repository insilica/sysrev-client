"""Sysrev OpenAPI Client - Auto-generated client for the Sysrev API."""

# Client classes
from .gen.client import AuthenticatedClient, Client

# Models - all data models used in inputs/outputs
from .gen.models import *

# Error types
from .gen.errors import *

# Type utilities
from .gen.types import *

# API Endpoints - Article operations
from .gen.api.article import create_article
from .gen.api.article import delete_article_suppression
from .gen.api.article import get_article
from .gen.api.article import set_article_suppression

# API Endpoints - Enterprise Billing operations
from .gen.api.enterprise_billing import get_enterprise_billing_usage

# API Endpoints - Label operations
from .gen.api.label import get_label
from .gen.api.label import new_label
from .gen.api.label import set_label

# API Endpoints - Org Billing operations
from .gen.api.org_billing import get_org_auto_label_billing
from .gen.api.org_billing import get_org_billing_subscription

# API Endpoints - Project operations
from .gen.api.project import create_project
from .gen.api.project import get_project
from .gen.api.project import get_project_export
from .gen.api.project import start_project_export

# API Endpoints - Source operations
from .gen.api.source import create_source

# API Endpoints - User operations
from .gen.api.user import get_user

# API Endpoints - User Billing operations
from .gen.api.user_billing import get_user_billing_settings
from .gen.api.user_billing import get_user_billing_subscription
from .gen.api.user_billing import get_user_billing_usage
from .gen.api.user_billing import update_user_billing_settings

# API Endpoints - Webhook operations
from .gen.api.webhook import create_webhook_endpoint
from .gen.api.webhook import delete_webhook_endpoint
from .gen.api.webhook import get_webhook_endpoint
from .gen.api.webhook import update_webhook_endpoint

__all__ = [
    # Client classes
    "AuthenticatedClient",
    "Client",
    # Error types
    "UnexpectedStatus",
    # Type utilities
    "File",
    "FileTypes",
    "RequestFiles",
    "Response",
    "UNSET",
    "Unset",
    # Models (from gen.models)
    "Article",
    "ArticleFullText",
    "ArticleFullTextContentBlob",
    "ArticleFullTextContentJson",
    "ArticleFullTextContentJsonJsonType1",
    "ArticleSuppressionType",
    "AutoArticleLabel",
    "AutoArticleLabelReasoningType0",
    "AutoLabelAnswer",
    "AutoLabelAnswerUpdatedRequest",
    "AutoLabelAnswerUpdatedRequestEventType",
    "AutoLabelRun",
    "BillingLimitStrategy",
    "BillingSubscription",
    "BillingUsagePeriod",
    "Blob",
    "CloneProjectInput",
    "CreateArticleInput",
    "CreateArticleInputCitation",
    "CreateEnterpriseInput",
    "CreateProjectInput",
    "CreateSourceInput",
    "CreateWebhookEndpointBody",
    "DeleteArticleSuppressionResponse200",
    "DeleteWebhookEndpointResponse200",
    "Enterprise",
    "Error",
    "ErrorResponse",
    "Label",
    "LabelSchemaType0",
    "LabelSettings",
    "LabelStat",
    "NewLabelBody",
    "NewLabelBodySchemaType0",
    "Org",
    "OrgInvite",
    "OrgProject",
    "OrgProjectAdminsItem",
    "OrgSettings",
    "Project",
    "ProjectBillingSettings",
    "ProjectBillingSettingsLimit",
    "ProjectBillingUsage",
    "ProjectExport",
    "ProjectExportStatus",
    "ProjectExportType",
    "ProjectInvite",
    "ProjectSettings",
    "SetArticleSuppressionBody",
    "SetArticleSuppressionResponse200",
    "SetLabelBody",
    "SetLabelBodySchemaType0",
    "Source",
    "StartProjectExportInput",
    "TransferProjectInput",
    "UpdateWebhookEndpointBody",
    "User",
    "UserBillingSettings",
    "UserBillingSettingsLimit",
    "UserBillingUsage",
    "WebhookEndpoint",
    "WebhookEventTypesItems",
    # API endpoint functions - Article
    "create_article",
    "delete_article_suppression",
    "get_article",
    "set_article_suppression",
    # API endpoint functions - Enterprise Billing
    "get_enterprise_billing_usage",
    # API endpoint functions - Label
    "get_label",
    "new_label",
    "set_label",
    # API endpoint functions - Org Billing
    "get_org_auto_label_billing",
    "get_org_billing_subscription",
    # API endpoint functions - Project
    "create_project",
    "get_project",
    "get_project_export",
    "start_project_export",
    # API endpoint functions - Source
    "create_source",
    # API endpoint functions - User
    "get_user",
    # API endpoint functions - User Billing
    "get_user_billing_settings",
    "get_user_billing_subscription",
    "get_user_billing_usage",
    "update_user_billing_settings",
    # API endpoint functions - Webhook
    "create_webhook_endpoint",
    "delete_webhook_endpoint",
    "get_webhook_endpoint",
    "update_webhook_endpoint",
]
