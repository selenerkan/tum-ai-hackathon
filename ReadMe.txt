Basis for this challenge is the publicly available easy-to-access dataset ChestX-ray
from NIH Clinical Center. It is too large to be used in the
Makeathon (ca. 42 GB). So, we reduced it to ca.10% of the original size. We also
only use simple clinical pictures, i.e., that multiple diagnoses are not included
and only pictures with only one diagnosis (Finding_Lables) are considered.

Whole ChestX-ray dataset: https://nihcc.app.box.com/v/ChestXray-NIHCC/folder/36938765345
Original paper: https://arxiv.org/pdf/1705.02315v5.pdf

Besides actual classification models, participants are encouraged to create ideas on
how to use these models in practice (e.g., app or framework). Thereby, special
conditions/challenges in the developing world can be considered, e.g.:

- Poor access to existing medical IT tools / less available computing power /
restricted access to internet and cloud computing / old smartphones
- Old X-ray devices, so that the quality of images might be much poorer as in the
training data set
- If the app/framework idea includes using smartphone pictures (or similar) of X-ray
images, how different photo quality and light conditions can be considered
- Workflow related challenges
- etc. 

There is a considerable amount of research dealing with the classification of X-ray
images (incl. works with ChestX-ray dataset), so, there is a lot of available material
for inspiration. Some form of transfer learning from pre-trained computer vision models
can be used e.g. ResNet-family or similar.

Note: the current csv-file (Dataset_Chest_X_Ray_Sample.csv) uses ";" as saparator and
"," for decimals (European convention)