from src.generators import pairs_generator_fast
from src.generators import pairs_generator_m_e
from src.generators import pairs_generator_short

# Реализация функций лежит в src/generators
if __name__ == "__main__":
    pairs_generator_short(3)
    pairs_generator_fast(3)
    pairs_generator_m_e(3)
