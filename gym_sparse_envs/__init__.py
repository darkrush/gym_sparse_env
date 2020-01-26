from gym.envs.registration import  register

register(
    id='SparseHalfCheetah-v2',
    entry_point='gym_sparse_envs.envs:SparseHalfCheetahEnv',
    max_episode_steps=1000,
)

register(
    id='SparseMountainCarContinuous-v0',
    entry_point='gym_sparse_envs.envs:SparseContinuous_MountainCarEnv',
    max_episode_steps=999,
    reward_threshold=99.0,
)

register(
    id='SparseHopper-v2',
    entry_point='gym_sparse_envs.envs:SparseHopperEnv',
    max_episode_steps=1000,
)

register(
    id='SparseReacher-v2',
    entry_point='gym_sparse_envs.envs:SparseReacherEnv',
    max_episode_steps=100,
)

register(
    id='SparsePendulum-v0',
    entry_point='gym_sparse_envs.envs:SparsePendulumEnv',
    max_episode_steps=200,
)

register(
    id='SparseSwimmer-v2',
    entry_point='gym_sparse_envs.envs:SparseSwimmerEnv',
    max_episode_steps=1000,
)