from modeltranslation.translator import translator, TranslationOptions
from .models import Product, Category


class ProductTransaltionOptions(TranslationOptions):
    fields = ('name', 'slug', 'description', )

class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', 'slug', )

translator.register(Product, ProductTransaltionOptions)
translator.register(Category, CategoryTranslationOptions)