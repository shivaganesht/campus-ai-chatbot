"""
Configuration Manager
======================
Handles campus customization and settings
"""

import os
import json
from typing import Dict, Any, Optional


class ConfigManager:
    """Manages campus configuration with easy customization"""
    
    def __init__(self, config_path: str = 'config/campus_config.json'):
        self.config_path = config_path
        self.config = self._load_config()
    
    def _load_config(self) -> Dict[str, Any]:
        """Load configuration from JSON file"""
        try:
            if os.path.exists(self.config_path):
                with open(self.config_path, 'r', encoding='utf-8') as f:
                    return json.load(f)
            return self._create_default_config()
        except Exception as e:
            print(f"⚠️  Config load error: {e}")
            return self._create_default_config()
    
    def _create_default_config(self) -> Dict[str, Any]:
        """Create default configuration"""
        default = {
            "campus_info": {
                "name": "Your University",
                "short_name": "YU",
                "tagline": "Excellence in Education"
            },
            "chatbot_settings": {
                "bot_name": "CampusBot",
                "welcome_message": "Hello! How can I help you?"
            },
            "branding": {
                "primary_color": "#1e3a8a",
                "secondary_color": "#3b82f6"
            }
        }
        os.makedirs(os.path.dirname(self.config_path), exist_ok=True)
        self._save_config(default)
        return default
    
    def _save_config(self, config: Dict[str, Any]) -> bool:
        """Save configuration to file"""
        try:
            with open(self.config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2)
            return True
        except Exception as e:
            print(f"❌ Config save error: {e}")
            return False
    
    def get_config(self) -> Dict[str, Any]:
        """Get full configuration"""
        return self.config
    
    def get_public_config(self) -> Dict[str, Any]:
        """Get configuration safe for frontend"""
        return self.config.copy()
    
    def update_config(self, updates: Dict[str, Any]) -> bool:
        """Update configuration with new values"""
        def deep_update(base: dict, updates: dict):
            for key, value in updates.items():
                if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                    deep_update(base[key], value)
                else:
                    base[key] = value
        
        deep_update(self.config, updates)
        return self._save_config(self.config)
    
    def get_value(self, *keys: str, default: Any = None) -> Any:
        """Get nested configuration value"""
        value = self.config
        for key in keys:
            if isinstance(value, dict) and key in value:
                value = value[key]
            else:
                return default
        return value
    
    def update_asset_path(self, asset_type: str, path: str) -> bool:
        """Update asset path in config"""
        asset_mapping = {
            'logo': ['branding', 'logo_path'],
            'favicon': ['branding', 'favicon_path'],
            'background': ['branding', 'background_image'],
            'bot_avatar': ['chatbot_settings', 'bot_avatar']
        }
        
        if asset_type in asset_mapping:
            keys = asset_mapping[asset_type]
            target = self.config
            for key in keys[:-1]:
                if key not in target:
                    target[key] = {}
                target = target[key]
            target[keys[-1]] = path
            return self._save_config(self.config)
        return False
    
    def get_department_info(self, department: str) -> Optional[Dict[str, str]]:
        """Get department contact information"""
        return self.config.get('departments', {}).get(department)
