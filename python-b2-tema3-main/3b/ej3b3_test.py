import logging
from ej3b3 import (
    DecoratorFactoryLogs,
    log_directory,
)  # Asegúrate de ajustar el import según tu estructura de proyecto
import os
from io import StringIO

# Ensuring the directory for logs exists
log_directory = "data/output/logs"
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


def test_log_decorator():
    factory = DecoratorFactoryLogs()
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)  # Adjunta el handler antes de la prueba

    @factory.log_decorator(message="Test Log Decorator:")
    def test_function():
        pass

    test_function()

    logger.removeHandler(handler)  # Limpieza: remover el handler después de la prueba
    logs = stream.getvalue()
    assert "Test Log Decorator:" in logs
    assert "Starting: test_function" in logs
    assert "Finishing: test_function" in logs


def test_debug_log_decorator():
    factory = DecoratorFactoryLogs()

    @factory.debug_log_decorator(message="Test Debug Decorator:")
    def test_function_debug(x):
        return x

    stream = StringIO()
    handler = logging.StreamHandler(stream)
    logger.addHandler(handler)

    test_function_debug(10)

    handler.flush()
    logs = stream.getvalue()
    assert "Test Debug Decorator:" in logs
    assert "Executing: test_function_debug" in logs
    assert "10" in logs  # Verifica que el argumento esté en los logs
    logger.removeHandler(handler)


def test_save_log_decorator():
    factory = DecoratorFactoryLogs()
    custom_log_path = f"{log_directory}/test_custom_log.log"

    @factory.save_log_decorator(
        message="Test Save Log Decorator:", filepath=custom_log_path
    )
    def test_function_save(x, y):
        return x + y

    test_function_save(2, 3)

    with open(custom_log_path, "r") as file:
        logs = file.read()

    assert "Test Save Log Decorator:" in logs
    assert "Executing: test_function_save" in logs
    assert "2" in logs and "3" in logs  # Verifica que los argumentos estén en los logs
    os.remove(custom_log_path)
