import tensorflow as tf

# 棋盘属性
WIDTH = 6
HEIGHT = 6
CHANNELS = 4
N_IN_ROW = 4

# 棋盘落子状态
BLACK = -1
WHITE = 1
EMPTY = 0

# 棋局结果
WIN = 1
LOSS = -1
TIE = 0
NOTHING = 2
COLOR = {
    BLACK: 'Black',
    WHITE: 'White',
    TIE: 'Tie'
}

# 训练超参数
MODEL_FILE = 'data/model.h5'
LEARNING_RATE = 3e-4
MAX_EPISODE = 10000
REWARD_GAMMA = 0.99
BUFFER_LENGTH = 10000
ENTROPY_BETA = 0.01
BATCH_SIZE = 512
EPOCHS = 5
CHECK_FREQ = 50

# GPU Config
gpus = tf.config.experimental.list_physical_devices(device_type='GPU')

for gpu in gpus:
    tf.config.experimental.set_memory_growth(device=gpu, enable=True)
