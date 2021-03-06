import numpy as np
from gym import utils
from gym.envs.mujoco import mujoco_env

class SparseSwimmerEnv(mujoco_env.MujocoEnv, utils.EzPickle):
    def __init__(self):
        self.control_penalty = 1.0
        mujoco_env.MujocoEnv.__init__(self, 'swimmer.xml', 4)
        utils.EzPickle.__init__(self)
        

    def set_control_coef(self,coef):
        self.control_penalty = coef
    def step(self, a):
        ctrl_cost_coeff = 0.1*self.control_penalty
        xposbefore = self.sim.data.qpos[0]
        self.do_simulation(a, self.frame_skip)
        xposafter = self.sim.data.qpos[0]
        if xposafter - self.init_qpos[0] > 1.0:
            reward_run = 1
        else:
            reward_run = 0
        #reward_fwd = (xposafter - xposbefore) / self.dt
        reward_ctrl = - ctrl_cost_coeff * np.square(a).sum()
        reward = reward_run + reward_ctrl
        ob = self._get_obs()
        return ob, reward, False, dict(reward_run=reward_run, reward_ctrl=reward_ctrl)

    def _get_obs(self):
        qpos = self.sim.data.qpos
        qvel = self.sim.data.qvel
        return np.concatenate([qpos.flat[2:], qvel.flat])

    def reset_model(self):
        self.set_state(
            self.init_qpos + self.np_random.uniform(low=-.1, high=.1, size=self.model.nq),
            self.init_qvel + self.np_random.uniform(low=-.1, high=.1, size=self.model.nv)
        )
        return self._get_obs()
