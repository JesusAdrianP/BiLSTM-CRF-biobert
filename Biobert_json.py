# coding=utf-8
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Lint as: python3
"""Introduction to the Biobert NER Shared Task:  Named Entity Recognition"""
import datasets
import json


logger = datasets.logging.get_logger(__name__)

_DESCRIPTION = """\
Este es un dataset biomédico Biobert para el español con 29 etiquetas"""

_URL="data/"
_TRAINING_FILE = "train.json"
_DEV_FILE = "valid.json"
_TEST_FILE = "test.json"


class Biobert_json_Config(datasets.BuilderConfig):
    

    def __init__(self, **kwargs):
        super(Biobert_json_Config, self).__init__(**kwargs)


class Conll2003(datasets.GeneratorBasedBuilder):
    """Conll2003 dataset."""

    BUILDER_CONFIGS = [
        Biobert_json_Config(name="Biobert_json", version=datasets.Version("1.0.0"), description="Biobert_json dataset"),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            description=_DESCRIPTION,
            features=datasets.Features(
                {
                   # "id": datasets.Value("string"),
                    "sentencia": datasets.Sequence(datasets.Value("string")),
                    "tag": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "B_CANCER_CONCEPT",
                                "B_CHEMOTHERAPY",
                                "B_DATE",
                                "B_DRUG",
                                "B_FAMILY",
                                "B_FREQ",
                                "B_IMPLICIT_DATE",
                                "B_INTERVAL",
                                "B_METRIC",
                                "B_OCURRENCE_EVENT",
                                "B_QUANTITY",
                                "B_RADIOTHERAPY",
                                "B_SMOKER_STATUS",
                                "B_STAGE", 
                                "B_SURGERY",
                                "B_TNM",
                                "I_CANCER_CONCEPT",
                                "I_DATE",
                                "I_DRUG",
                                "I_FAMILY",
                                "I_FREQ",
                                "I_IMPLICIT_DATE",
                                "I_INTERVAL",
                                "I_METRIC",
                                "I_OCURRENCE_EVENT",
                                "I_SMOKER_STATUS",
                                "I_STAGE", 
                                "I_SURGERY",
                                "I_TNM",
                                "O", 
                                
                            ]
                        )
                    ),
                }
            ),
            supervised_keys=None,
        )

    def _split_generators(self, dl_manager):
        """Returns SplitGenerators."""
        urls_to_download = {
            "train": f"{_URL}{_TRAINING_FILE}",
            "val": f"{_URL}{_DEV_FILE}",
            "test": f"{_URL}{_TEST_FILE}",
        }
        downloaded_files = dl_manager.download_and_extract(urls_to_download)

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": downloaded_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": downloaded_files["val"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": downloaded_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            for line in f:  
                record = json.loads(line)   
                yield guid, record
                guid += 1
            
           