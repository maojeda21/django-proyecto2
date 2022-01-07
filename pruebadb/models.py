from django.db import models

class Empresa(models.Model):
    nombre = models.CharField(max_length=20)
    fundacion = models.IntegerField()
    
    # Representación de los caractres de los modelos.
    def __str__(self) -> str:
        return self.nombre
        #return super().__str__()


class Programador(models.Model):
    nombre = models.CharField(max_length=40) 
    # Foreingkey: llave foranea con la clase Empresa
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE) # on_delete: indica que si elminamos una empresa se eliminaria los dev

    def __str__(self) -> str:
        return self.nombre, self.empresa
    
    