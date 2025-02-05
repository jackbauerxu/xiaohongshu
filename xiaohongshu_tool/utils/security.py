"""
安全加密模块
使用Fernet实现敏感信息加密
"""
from cryptography.fernet import Fernet
from pydantic import BaseModel, validator
from xiaohongshu_tool.config import load_config

class Encryptor:
    def __init__(self, key):
        self.cipher = Fernet(key)
    
    def encrypt(self, data: str) -> bytes:
        return self.cipher.encrypt(data.encode())
    
    def decrypt(self, token: bytes) -> str:
        return self.cipher.decrypt(token).decode()

class RequestValidator(BaseModel):
    """请求参数验证模型"""
    task_type: str
    priority: int
    params: dict

    @validator('priority')
    def priority_range(cls, v):
        if v < 1 or v > 3:
            raise ValueError('Priority must be between 1-3')
        return v 

# 敏感字段自动加密装饰器
def encrypt_fields(func):
    def wrapper(*args, **kwargs):
        config = load_config()
        if config.security.encryption_enabled:
            encryptor = Encryptor(config.security.fernet_key)
            for field in config.security.sensitive_fields:
                if field in kwargs:
                    kwargs[field] = encryptor.encrypt(kwargs[field])
        return func(*args, **kwargs)
    return wrapper 