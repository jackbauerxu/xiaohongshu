"""
系统监控模块
集成Prometheus和Grafana
"""
from prometheus_client import start_http_server, Gauge, Counter

class SystemMetrics:
    def __init__(self):
        self.task_queue_size = Gauge('xhs_task_queue_size', 'Current task queue size')
        self.request_errors = Counter('xhs_request_errors', 'Total request errors')
        
    def start_monitoring(self, port=9090):
        """启动监控服务端"""
        start_http_server(port)

class HealthCheck:
    def __init__(self):
        self.health_status = Gauge('xhs_health_status', 'Service health status')
        
    def update_status(self, status_code):
        self.health_status.set(status_code) 