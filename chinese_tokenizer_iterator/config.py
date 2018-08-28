from chinese_tokenizer_iterator.tokenizers import (
    tokenizer_jieba,
    tokenizer_thulac,
    tokenizer_nlpir,
    tokenizer_ltp
)

tokenizer_registry = {
    'jieba': tokenizer_jieba,
    'thulac': tokenizer_thulac,
    'nlpir': tokenizer_nlpir,
    'ltp': tokenizer_ltp
}
