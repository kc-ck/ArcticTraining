# Copyright 2025 Snowflake Inc.
# SPDX-License-Identifier: Apache-2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import computed_field

from arctic_training.logging import logger


class BaseConfig(BaseModel):
    def __init__(self, **data):
        logger.info(f"Initializing {self.__class__.__name__}")
        super().__init__(**data)

    model_config = ConfigDict(
        extra="forbid",
        use_enum_values=True,
        # validate_assignment=True,
        validate_default=True,
        use_attribute_docstrings=True,
        populate_by_name=True,
    )

    @computed_field  # type: ignore[prop-decorator]
    @property
    def local_rank(self) -> int:
        return int(os.getenv("LOCAL_RANK", 0))

    @computed_field  # type: ignore[prop-decorator]
    @property
    def global_rank(self) -> int:
        return int(os.getenv("RANK", 0))

    @computed_field  # type: ignore[prop-decorator]
    @property
    def world_size(self) -> int:
        return int(os.getenv("WORLD_SIZE", 1))
