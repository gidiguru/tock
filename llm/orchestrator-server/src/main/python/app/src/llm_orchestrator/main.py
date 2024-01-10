#   Copyright (C) 2023-2024 Credit Mutuel Arkea
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#
from fastapi import FastAPI

from llm_orchestrator.errors.exceptions.exceptions import (
    GenAIOrchestratorException,
)
from llm_orchestrator.errors.handlers.fastapi.fastapi_handler import (
    business_exception_handler,
    generic_exception_handler,
)
from llm_orchestrator.routers.app_monitors_router import (
    application_check_router,
)
from llm_orchestrator.routers.em_providers_router import em_providers_router
from llm_orchestrator.routers.llm_providers_router import llm_providers_router
from llm_orchestrator.routers.rag_router import rag_router

app = FastAPI(title='Generative AI Orchestrator')

# Add functional exception handler
app.add_exception_handler(GenAIOrchestratorException, business_exception_handler)
app.add_exception_handler(Exception, generic_exception_handler)

app.include_router(application_check_router)
app.include_router(llm_providers_router)
app.include_router(em_providers_router)
app.include_router(rag_router)