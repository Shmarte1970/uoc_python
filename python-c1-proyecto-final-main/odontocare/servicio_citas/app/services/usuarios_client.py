"""
Cliente REST para comunicarse con el Servicio de Usuarios
Este módulo NO accede directamente a la base de datos de usuarios,
solo consume la API REST del servicio de usuarios
"""
import requests
from flask import current_app


class UsuariosServiceClient:
    """
    Cliente para consumir el servicio de usuarios vía REST
    Implementa la comunicación entre microservicios
    """

    @staticmethod
    def get_base_url():
        """Obtiene la URL base del servicio de usuarios"""
        return current_app.config.get('SERVICIO_USUARIOS_URL', 'http://localhost:5001')

    @staticmethod
    def validar_token(token):
        """
        Valida un token JWT con el servicio de usuarios

        Args:
            token: Token JWT a validar

        Returns:
            dict con información del usuario o None si es inválido
        """
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/auth/validate"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error validando token: {e}")
            return None

    @staticmethod
    def obtener_doctor(id_doctor, token):
        """
        Obtiene información de un doctor desde el servicio de usuarios

        Args:
            id_doctor: ID del doctor
            token: Token JWT para autenticación

        Returns:
            dict con información del doctor o None
        """
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/admin/doctores/{id_doctor}"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error obteniendo doctor: {e}")
            return None

    @staticmethod
    def obtener_paciente(id_paciente, token):
        """
        Obtiene información de un paciente desde el servicio de usuarios

        Args:
            id_paciente: ID del paciente
            token: Token JWT para autenticación

        Returns:
            dict con información del paciente o None
        """
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/admin/pacientes/{id_paciente}"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error obteniendo paciente: {e}")
            return None

    @staticmethod
    def obtener_centro(id_centro, token):
        """
        Obtiene información de un centro desde el servicio de usuarios

        Args:
            id_centro: ID del centro
            token: Token JWT para autenticación

        Returns:
            dict con información del centro o None
        """
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/admin/centros/{id_centro}"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error obteniendo centro: {e}")
            return None

    @staticmethod
    def listar_doctores(token):
        """Lista todos los doctores"""
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/admin/doctores"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error listando doctores: {e}")
            return None

    @staticmethod
    def listar_pacientes(token):
        """Lista todos los pacientes"""
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/admin/pacientes"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error listando pacientes: {e}")
            return None

    @staticmethod
    def listar_centros(token):
        """Lista todos los centros"""
        try:
            url = f"{UsuariosServiceClient.get_base_url()}/admin/centros"
            headers = {'Authorization': f'Bearer {token}'}
            response = requests.get(url, headers=headers, timeout=5)

            if response.status_code == 200:
                return response.json()
            return None
        except requests.RequestException as e:
            current_app.logger.error(f"Error listando centros: {e}")
            return None
