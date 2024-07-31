from os import system
from time import sleep
from utils.translator import translatorHTML
from utils.copyFunction import copy_to_clipboard
system('cls')
html_content = '''
<p>La estructura de créditos del programa de <strong>Rendimiento Deportivo: de la Valoración a la Optimización</strong> se recoge en la siguiente tabla. Hay que reseñar que la duración es meramente orientativa, pues la metodología seguida integra el conocimiento y habilidades a adquirir en cada parte, mediante ejercicios integradores de adquisición de conocimiento e interiorización de prácticas proyectuales:</p>

<div class="table-responsive">
<table class="table table--format table--format__1">
	<thead>
		<tr>
			<th>MÓDULOS</th>
			<th>CRÉDITOS ECTS<sup>a</sup></th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>1ª Parte: Sesiones Presenciales</td>
			<td>25</td>
		</tr>
		<tr>
			<td>2ª Parte: Proyecto de Alto Rendimiento</td>
			<td>5</td>
		</tr>
	</tbody>
	<tfoot>
		<tr>
			<td>TOTAL</td>
			<td>30</td>
		</tr>
	</tfoot>
</table>

<p>a. La equivalencia en créditos puede variar según la universidad donde se haya inscrito. Un (1) crédito ECTS (European Credit Transfer System) equivale a 10 + 15 horas. Si el alumno cursa el Programa matriculado en una universidad no perteneciente al Espacio Europeo de Educación Superior (EEES), la relación entre créditos - horas, puede variar.</p>
</div>

<h2>Duración</h2>

<p>La&nbsp;<strong>Rendimiento Deportivo: de la Valoración a la Optimización&nbsp;</strong>tiene&nbsp;<strong>30 créditos</strong>. La duración del&nbsp;<strong>Rendimiento Deportivo: de la Valoración a la Optimización&nbsp;</strong>es de&nbsp;<strong>9&nbsp;a 12&nbsp;meses</strong>. En este período de tiempo, el alumno tiene que haber superado con éxito todas las actividades evaluadas y aprobado el Proyecto Final.</p>
'''

while True:
    system('cls')
    print('Welcome to Titanic! \n------------------------------------- \n1.FR \n2.EN \n3.PT \n')

    menu_select= int(input('Please select one option of the menu: '))

    if menu_select==1:
        system('cls')
        frHtml = translatorHTML(html_content,'fr')
        copy_to_clipboard(frHtml)

    elif menu_select==2:
        system('cls')
        enHtml = translatorHTML(html_content,'en')
        copy_to_clipboard(enHtml)
    elif menu_select==3:
        system('cls')
        ptHtml = translatorHTML(html_content,'pt')
        copy_to_clipboard(ptHtml)

    else:
        system('cls')
        print('Error of select menu')
        sleep(1)