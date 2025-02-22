#  Copyright (c) 2022 EPAM Systems
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#  https://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License

from typing import Any, Callable, ByteString, Dict, IO, List, Optional, Text, \
    Union, Tuple

from reportportal_client.core.rp_file import RPFile as RPFile
from reportportal_client.core.rp_issues import Issue as Issue
from reportportal_client.core.rp_responses import RPResponse as RPResponse
from reportportal_client.static.abstract import AbstractBaseClass
from reportportal_client.static.defines import Priority as Priority


class HttpRequest:
    session_method: Callable = ...
    url: Text = ...
    files: Optional[Dict] = ...
    data: Optional[Union[Dict, List[Union[tuple, ByteString]], IO]] = ...
    json: Optional[Dict] = ...
    verify_ssl: Optional[bool] = ...
    http_timeout: Union[float, Tuple[float, float]] = ...
    name: Optional[Text] = ...

    def __init__(self,
                 session_method: Callable,
                 url: Text,
                 data=Optional[
                     Union[Dict, List[Union[tuple, ByteString, IO]]]],
                 json=Optional[Dict],
                 files=Optional[Dict],
                 verify_ssl=Optional[bool],
                 name=Optional[Text]) -> None: ...

    def make(self) -> Optional[RPResponse]: ...


class RPRequestBase(metaclass=AbstractBaseClass):
    __metaclass__: AbstractBaseClass = ...
    _http_request: Optional[HttpRequest] = ...
    _priority: Priority = ...
    _response: Optional[RPResponse] = ...

    def __init__(self) -> None: ...

    def __lt__(self, other: RPRequestBase) -> bool: ...

    @property
    def http_request(self) -> HttpRequest: ...

    @http_request.setter
    def http_request(self, value: HttpRequest) -> None: ...

    @property
    def priority(self) -> Priority: ...

    @priority.setter
    def priority(self, value: Priority) -> None: ...

    @property
    def response(self) -> Optional[RPResponse]: ...

    @response.setter
    def response(self, value: RPResponse) -> None: ...

    def payload(self) -> Dict: ...


class LaunchStartRequest(RPRequestBase):
    attributes: Optional[Union[List, Dict]] = ...
    description: Text = ...
    mode: Text = ...
    name: Text = ...
    rerun: bool = ...
    rerun_of: Text = ...
    start_time: Text = ...
    uuid: Text = ...

    def __init__(self,
                 name: Text,
                 start_time: Text,
                 attributes: Optional[Union[List, Dict]] = ...,
                 description: Optional[Text] = ...,
                 mode: Text = ...,
                 rerun: bool = ...,
                 rerun_of: Optional[Text] = ...,
                 uuid: Optional[Text] = ...) -> None: ...

    @property
    def payload(self) -> Dict: ...


class LaunchFinishRequest(RPRequestBase):
    attributes: Optional[Union[List, Dict]] = ...
    description: Text = ...
    end_time: Text = ...
    status: Text = ...

    def __init__(self,
                 end_time: Text,
                 status: Optional[Text] = ...,
                 attributes: Optional[Union[List, Dict]] = ...,
                 description: Optional[Text] = ...) -> None: ...

    @property
    def payload(self) -> Dict: ...


class ItemStartRequest(RPRequestBase):
    attributes: Optional[Union[List, Dict]] = ...
    code_ref: Text = ...
    description: Text = ...
    has_stats: bool = ...
    launch_uuid: Text = ...
    name: Text = ...
    parameters: Optional[Union[List, Dict]] = ...
    retry: bool = ...
    start_time: Text = ...
    test_case_id: Optional[Text] = ...
    type_: Text = ...
    uuid: Text = ...
    unique_id: Text = ...

    def __init__(self,
                 name: Text,
                 start_time: Text,
                 type_: Text,
                 launch_uuid: Text,
                 attributes: Optional[Union[List, Dict]] = ...,
                 code_ref: Optional[Text] = ...,
                 description: Optional[Text] = ...,
                 has_stats: bool = ...,
                 parameters: Optional[Union[List, Dict]] = ...,
                 retry: bool = ...,
                 test_case_id: Optional[Text] = ...,
                 uuid: Optional[Any] = ...,
                 unique_id: Optional[Any] = ...) -> None: ...

    @property
    def payload(self) -> Dict: ...


class ItemFinishRequest(RPRequestBase):
    attributes: Optional[Union[List, Dict]] = ...
    description: Text = ...
    end_time: Text = ...
    is_skipped_an_issue: bool = ...
    issue: Issue = ...
    launch_uuid: Text = ...
    status: Text = ...
    retry: bool = ...

    def __init__(self,
                 end_time: Text,
                 launch_uuid: Text,
                 status: Text,
                 attributes: Optional[Union[List, Dict]] = ...,
                 description: Optional[Any] = ...,
                 is_skipped_an_issue: bool = ...,
                 issue: Optional[Issue] = ...,
                 retry: bool = ...) -> None: ...

    @property
    def payload(self) -> Dict: ...


class RPRequestLog(RPRequestBase):
    file: RPFile = ...
    launch_uuid: Text = ...
    level: Text = ...
    message: Text = ...
    time: Text = ...
    item_uuid: Text = ...

    def __init__(self,
                 launch_uuid: Text,
                 time: Text,
                 file: Optional[RPFile] = ...,
                 item_uuid: Optional[Text] = ...,
                 level: Text = ...,
                 message: Optional[Text] = ...) -> None: ...

    def __file(self) -> Dict: ...

    @property
    def payload(self) -> Dict: ...

    @property
    def multipart_size(self) -> int: ...


class RPLogBatch(RPRequestBase):
    default_content: Text = ...
    log_reqs: List[RPRequestLog] = ...

    def __init__(self, log_reqs: List[RPRequestLog]) -> None: ...

    def __get_file(self, rp_file: RPFile) -> tuple: ...

    def __get_files(self) -> List: ...

    def __get_request_part(self) -> Dict: ...

    @property
    def payload(self) -> Dict: ...
