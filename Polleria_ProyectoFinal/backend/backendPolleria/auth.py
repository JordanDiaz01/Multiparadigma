from models import Empleado
from flask import request,jsonify
from functools import wraps

def obtenerInfo(token):
    if token:
        resp=Empleado.decode_auth_token(token)
        user=Empleado.query.filter_by(idEmpleado=resp).first()
        if user:
            infoEmpleado={
                'status':'success',
                'data':{
                    'user_id':user.idEmpleado,
                    'email':user.email,
                    'admin':user.admin
                }
            }
            return infoEmpleado
        else:
            error ={
                'status':'fail',
                'message':resp
            }
            return error
        
def tokenCheck(f):
    @wraps(f)
    def verificar(*args,**kwargs):
        token = None
        if 'token' in request.headers:
            token = request.headers['token']
        if not token:  
            return jsonify({'message':'token no encontrado'})
        try:
            info= obtenerInfo(token)
            if info['status'] =='fail':
                return jsonify({'message':'token invalido'})
        except:
            return jsonify({'message':'token invalido'})
        return f(info['data'],*args,**kwargs)
    return verificar

def verificarToken(token):
        if not token:  
            return jsonify({'message':'token no encontrado'})
        try:
            info= obtenerInfo(token)
            if info['status'] =='fail':
                return jsonify({'message':'token invalido'})
        except:
            return jsonify({'message':'token invalido'})
        return info