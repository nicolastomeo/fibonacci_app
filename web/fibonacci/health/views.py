from flask import jsonify
from fibonacci import cache
from fibonacci import db
from fibonacci.health import health
import psutil


@health.route('/health')
def health_check():
    """
    Check status of application (successful if health answers), database and redis
    as well as some stats about cpu, disk and memory.
    :return Json with info about the service:
    """
    status_app = {'status': 'Connection Successful'}
    try:
        cache.cache._client.info()
        status_redis = {'status': 'Connection Successful'}
    except:
        status_redis = {'status': 'Connection Failed'}
    try:
        db.session.execute('SELECT 1;')
        db.session.commit();
        status_db = {'status': 'Connection Successful'}
    except:
        status_db = {'status': 'Connection Failed'}
    cpu_usage = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    memory_stats = {'total': virtual_memory.total, 'available': virtual_memory.available,
                    'percent': virtual_memory.percent}
    disk_usage = psutil.disk_usage('/')
    disk_stats = {'total': disk_usage.total, 'used': disk_usage.used, 'free': disk_usage.free,
                  'percent': disk_usage.percent}
    return jsonify({'application': status_app, 'redis': status_redis, 'database': status_db, 'cpu_usage': cpu_usage,
                    'memory_stats': memory_stats, 'disk_stats': disk_stats})
