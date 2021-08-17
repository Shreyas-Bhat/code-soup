import unittest

import torch
import torch.nn as nn

from code_soup.common.vision.models.allconvnet import AllConv, AllConvNet


class AllConvModel(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.model = AllConv(
            image_size=96, n_classes=1, device=torch.device("cpu"), lr=0.01
        )

    def test_step(self):
        self.model.step([torch.randn(96, 96, 3, 3), torch.ones(4)])
