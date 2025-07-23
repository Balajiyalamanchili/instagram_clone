# from django_elasticsearch_dsl import Document, Index, fields
# from django_elasticsearch_dsl.registries import registry


# from django.contrib.auth.models import User


# # user Index
# @registry.register_document
# class UserDocument(Document):
#     # user = fields.ObjectField(properties={
#     #     'user_name':fields.TextField(),
#     # })

#     class Index:
#         name = 'users'

#     class Django:
#         model= User
#         fields = ['username']






## Analyzer to get matches in singkle letter also


from django_elasticsearch_dsl import Document, Index, fields
from django_elasticsearch_dsl.registries import registry
from django.contrib.auth.models import User
from elasticsearch_dsl.analysis import analyzer, token_filter

# Define edge ngram analyzer
edge_ngram_filter = token_filter(
    'edge_ngram_filter',
    type='edge_ngram',
    min_gram=1,
    max_gram=20
)

edge_ngram_analyzer = analyzer(
    'edge_ngram_analyzer',
    tokenizer='standard',
    filter=['lowercase', edge_ngram_filter]
)

@registry.register_document
class UserDocument(Document):
    username = fields.TextField(analyzer=edge_ngram_analyzer)

    class Index:
        name = 'users'

    class Django:
        model = User
        fields = []









