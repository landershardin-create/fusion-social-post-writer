# fusion_agent/agent.py

import logging
from typing import Dict, Optional, Any

logger = logging.getLogger("fusion_agent")

class FusionAgent:
    def __init__(self, config: Optional[Dict[str, Any]] = None):
        self.config = config or {}
        self.modules = {}
        self.session_context = {}
        self.roles = {}
        logger.info("FusionAgent initialized.")

    def register_module(self, name: str, module: Any):
        if name in self.modules:
            logger.warning(f"Module '{name}' already registered. Overwriting.")
        self.modules[name] = module
        logger.info(f"Module '{name}' registered.")

    def set_session_context(self, user_id: str, context: Dict[str, Any]):
        self.session_context[user_id] = context
        logger.debug(f"Session context set for user '{user_id}'.")

    def get_session_context(self, user_id: str) -> Dict[str, Any]:
        return self.session_context.get(user_id, {})

    def assign_role(self, user_id: str, role: str):
        self.roles[user_id] = role
        logger.debug(f"Role '{role}' assigned to user '{user_id}'.")

    def get_role(self, user_id: str) -> Optional[str]:
        return self.roles.get(user_id)

    def execute(self, user_id: str, module_name: str, action: str, **kwargs):
        module = self.modules.get(module_name)
        if not module:
            logger.error(f"Module '{module_name}' not found.")
            raise ValueError(f"Module '{module_name}' not registered.")
        
        role = self.get_role(user_id)
        context = self.get_session_context(user_id)

        logger.info(f"Executing '{action}' in module '{module_name}' for user '{user_id}' with role '{role}'.")

        if hasattr(module, "execute"):
            return module.execute(action, role=role, context=context, **kwargs)
        else:
            logger.error(f"Module '{module_name}' does not support 'execute'.")
            raise NotImplementedError(f"Module '{module_name}' missing 'execute' method.")
