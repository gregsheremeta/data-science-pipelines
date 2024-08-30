# Copyright 2024 The Kubeflow Authors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""Pipeline-level config options."""


class PipelineConfig:
    """PipelineConfig contains pipeline-level config options."""

    def __init__(self):
        self.semaphore_name = None

    def set_semaphore_name(self, semaphore_name: str):
        """Limit the parallel execution of pipelines that reference this semaphore.
        Args:
          semaphore_name: Name of the semaphore. In Argo Workflows, this is the name of a
          ConfigMap that defines the semaphore.
        """
        self.semaphore_name = semaphore_name
        return self
