# Copyright 2021-2024 Avaiga Private Limited
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with
# the License. You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on
# an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the
# specific language governing permissions and limitations under the License.

FROM python:3.11

WORKDIR /app

# Install application dependencies.
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy the application source code.
COPY main.css .
COPY main.py .
COPY .env .

CMD ["taipy", "run", "--no-debug", "--no-reloader", "main.py", "-H", "0.0.0.0", "-P", "5000"]