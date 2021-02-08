from pypinyin import pinyin, lazy_pinyin, Style

print(
    pinyin('中心'),
    pinyin('中心', heteronym=True),
    pinyin('中心', style=Style.FIRST_LETTER),
    pinyin('中心', style=Style.TONE2, heteronym=True),
    pinyin('中心', style=Style.TONE3, heteronym=True),
    pinyin('中心', style=Style.BOPOMOFO),
    lazy_pinyin('中心'),
    lazy_pinyin('战略', v_to_u=True),
    lazy_pinyin('衣裳', style=Style.TONE3, neutral_tone_with_five=True),
)
