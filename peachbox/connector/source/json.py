# Copyright 2015 Philipp Pahl, Sven Schubert
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

import peachbox

class JSON(object):
    """Source for JSON files."""

    def __init__(self):
        self.path = None

    def set_param(self, param):
        """Expects param['path']"""
        if param.get('path'):
            self.path = param['path']
        else:
            raise ValueError('Missing key in param: path')

    def data_frame(self):
        return peachbox.Spark.Instance().sql_context().jsonFile(self.path)
