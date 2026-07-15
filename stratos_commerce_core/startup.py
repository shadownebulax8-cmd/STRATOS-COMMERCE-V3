from stratos_commerce_core.config.settings import settings


def startup_banner() -> dict:
    return {
        "project": settings.project_name,
        "environment": settings.environment,
        "tenant_map": settings.tenant_subdomain_map,
        "redis": settings.redis_url,
        "database": settings.database_base_url,
    }
