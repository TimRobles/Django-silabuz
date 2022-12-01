from django.db import models

# Create your models here.

class Persona(models.Model):
    # id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'
        abstract = True

    @property
    def full_name(self):
        return self.first_name + " " + self.last_name

    def nombre_dni(self):
        return self.last_name + " " + self.first_name

    def __str__(self):
        return self.full_name + "-" + str(self.id)

class Salon(models.Model):
    # id = models.AutoField(primary_key=True)
    aula = models.CharField(max_length=2)
    hora_entrada = models.TimeField()
    idProfesor = models.ForeignKey('myapp.Profesor', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Salon'
        verbose_name_plural = 'Salones'
        ordering = [
            'hora_entrada',
        ]


class Profesor(Persona):
    
    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields = ['first_name', 'last_name'], name = 'primary_key_profesor'
            )
        ]

    def __str__(self):
        return self.full_name



class Alumno(Persona):
    idSalon = models.ForeignKey(Salon, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Alumno'
        verbose_name_plural = 'Alumnos'
        constraints = [
            models.UniqueConstraint(
                fields = ['first_name', 'last_name'], name = 'primary_key_alumno'
            )
        ]


class OrderedAlum(Alumno):
    class Meta:
        ordering = [
            "first_name",
            "-last_name",
            ]
        proxy = True