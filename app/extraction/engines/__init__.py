from .rules_engine import RulesEngine
from ..registry import register
register(RulesEngine())

# Optional future:
# from .langextract_engine import LangExtractEngine
# register(LangExtractEngine())