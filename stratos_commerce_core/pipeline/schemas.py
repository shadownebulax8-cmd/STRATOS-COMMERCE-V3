from typing import Optional

from pydantic import BaseModel, Field


class MerchantCreateRequest(BaseModel):
    tenant_id: str = Field(..., min_length=3, max_length=64)
    legal_name: str = Field(..., min_length=2, max_length=255)
    subdomain: str = Field(..., min_length=2, max_length=100)


class ProductCreateRequest(BaseModel):
    merchant_id: int
    sku: str = Field(..., min_length=1, max_length=100)
    name: str = Field(..., min_length=1, max_length=255)
    stock_quantity: int = Field(default=0, ge=0)
    price_cents: int = Field(default=0, ge=0)


class OrderPlacementRequest(BaseModel):
    merchant_id: int
    product_id: int
    quantity: int = Field(..., ge=1)
    currency: str = Field(default="usd")


class InventorySnapshot(BaseModel):
    product_id: int
    available_stock: int
    updated_at: Optional[str] = None
