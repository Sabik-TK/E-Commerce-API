from rest_framework.routers import DefaultRouter

from apps.category.views import (
    MainCategoryViewSet,
    CategoryViewSet
)

from apps.product.views import (
    ProductViewSet
)

from apps.accounts.views import (
    UserViewSet   
)


router = DefaultRouter()

router.register(r'account', UserViewSet,basename='account')
router.register(r'product', ProductViewSet,basename='product')
router.register(r'main-category', MainCategoryViewSet,basename='main-category')
router.register(r'category', CategoryViewSet,basename='category')
