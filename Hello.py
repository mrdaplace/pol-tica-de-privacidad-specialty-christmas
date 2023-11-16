# Copyright (c) Streamlit Inc. (2018-2022) Snowflake Inc. (2022)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import streamlit as st
from streamlit.logger import get_logger

LOGGER = get_logger(__name__)


def run():
    st.set_page_config(
        page_title="Política de privacidad",
        page_icon="",
    )



    st.markdown(
        """
# Política de privacidad
### 1 - ¿Qué hacemos con tu información?
Cuando compras algo de nuestra tienda, como parte del proceso de compra venta, nosotros recolectamos la información personal que nos das tales como nombre, dirección y correo electrónico.

Cuando navegas en nuestra tienda, también recibimos de manera automática la dirección de protocolo de internet de tu computadora (IP) con el fin de proporcionarnos información que nos ayuda a conocer acerca de su navegador y sistema operativo.

Email marketing (si aplicase): Con tu permiso, podremos enviarte correos electrónicos acerca de nuestra tienda, nuevos productos y otras actualizaciones


### 2 - Consentimiento

Cuando nos provees tu información personal para completar una transacción, verificar tu tarjeta de crédito, crear una orden, concertar un envío o hacer una devolución, implicamos que aceptas la recolección y uso por esa razón específica solamente.

Si te pedimos tu información personal por una razón secundaria, como marketing, te pediremos directamente tu expreso consentimiento, o te daremos la oportunidad de negarte.

¿Cómo puedo anular mi consentimiento?
Si luego de haber aceptado cambias de opinión, puedes anular tu consentimiento para que te contactemos, por la recolección, uso o divulgación de tu información, en cualquier momento, contactándonos a hey@moonplace.eu
### 3 - Divulgación
Podemos divulgar tu información personal si se nos requiere por ley o si violas nuestros Términos de Servicio.

### 4 - Stripe
Nuestra tienda se encuentra alojada en Stripe Payments. Ellos nos proporcionan la plataforma de comercio electrónico en línea que nos permite venderte nuestros productos y servicios.

Tus datos se almacenan a través del almacenamiento de datos de Stripe, bases de datos y la aplicación general de Stripe. Tus datos se almacenan en un servidor seguro detrás de un cortafuegos.

Payment:
Si eliges una pasarela de pago directo para completar tu compra, entonces Stripe almacena datos de tu tarjeta de crédito. Está cifrada a través de la Seguridad Standard de Datos de la Industria de Tarjetas de Pago (PCI-DSS). Tus datos de transacción de compra se almacenan sólo en la medida en que sea necesario para completar la transacción de compra. Después de que se haya completado, se borra la información de su transacción de compra.

Todas las pasarelas de pago directo se adhieren a los estándares establecidos por PCI-DSS como lo indicado por el Consejo de Normas de Seguridad de PCI, que es un esfuerzo conjunto de marcas como Visa, MasterCard, American Express y Discover.

Los requisitos del PCI-DSS ayudan a garantizar el manejo seguro de la información de tarjetas de crédito de las tiendas y sus proveedores de servicios.

Para una visión más clara, es posible que también desees leer las Condiciones de servicio de Stripe aquí o Declaración de privacidad aquí.

### 5 - Servicios de terceras partes
En general, los proveedores de terceras partes utilizados por nosotros solo recopilarán, usarán y divulgarán tu información en la medida que sea necesaria para que les permita desempeñar los servicios que nos proveen.

Sin embargo, algunos proveedores de servicios de terceros, tales como pasarelas de pago y otros procesadores de transacciones de pago, tienen sus propias políticas de privacidad con respecto a la información que estamos obligados a proporcionarles para las transacciones relacionadas con las compras.

Para estos proveedores, te recomendamos que leas las políticas de privacidad para que puedas entender la manera en que tu información personal será manejada.

En particular, recuerda que algunos proveedores pueden estar ubicados o contar con instalaciones que se encuentran en una jurisdicción diferente a ti o nosotros. Así que si deseas proceder con una transacción que involucra los servicios de un proveedor a terceros, tu información puede estar sujeta a las leyes de la jurisdicción (jurisdicciones) en que se encuentra el proveedor de servicios o sus instalaciones.

A modo de ejemplo, si te encuentras en Canadá y tu transacción es procesada por una pasarela de pago con sede en Estados Unidos, entonces tu información personal utilizada para completar la transacción puede ser sujeto de divulgación en virtud de la legislación de Estados Unidos, incluyendo la Ley Patriota.

Una vez que abandonas el sitio web de nuestra tienda o te re diriges a un sitio o aplicación de terceros, ya no estás siendo regulados por la presente Política de Privacidad o los Términos de Servicio de nuestra página web.

Enlaces
Cuando haces clic en enlaces de nuestra tienda, puede que seas re dirigido fuera de nuestro sitio. No somos responsables por las prácticas de privacidad de otros sitios y te recomendamos leer sus normas de privacidad.

### 6 - Seguridad
Para proteger tu información personal, tomamos precauciones razonables y seguimos las mejores prácticas de la industria para asegurarnos de que no haya pérdida de manera inapropiada, mal uso, acceso, divulgación, alteración o destrucción de la misma.

SI nos proporcionas la información de tu tarjeta de crédito, dicha información es encriptada mediante la tecnología Secure Socket Layer (SSL) y se almacena con un cifrado AES-256. Aunque ningún método de transmisión a través de Internet o de almacenamiento electrónico es 100% seguro, seguimos todos los requisitos de PCI-DSS e implementamos normas adicionales aceptadas por la industria.
COOKIES

Aquí tienes una lista de cookies que utilizamos. Las listamos para que puedas elegir si quieres optar por quitarlas o no.

_session_id, unique token, sessional, Allows Stripe to store information about your session (referrer, landing page, etc).

_Stripe_visit, no data held, Persistent for 30 minutes from the last visit, Used by our website provider’s internal stats tracker to record the number of visits

_Stripe_uniq, no data held, expires midnight (relative to the visitor) of the next day, Counts the number of visits to a store by a single customer.

cart, unique token, persistent for 2 weeks, Stores information about the contents of your cart.

_secure_session_id, unique token, sessional

storefront_digest, unique token, indefinite If the shop has a password, this is used to determine if the current visitor has access.

### 7 - Edad de consentimiento
Al utilizar este sitio, declaras que tienes al menos la mayoría de edad en tu estado o provincia de residencia, o que tienes la mayoría de edad en tu estado o provincia de residencia y que nos has dado tu consentimiento para permitir que cualquiera de tus dependientes menores use este sitio.

### 8 - Cambios en esta política de privacidad
Nos reservamos el derecho de modificar esta política de privacidad en cualquier momento, asÍ que por favor revísala frecuentemente. Cambios y aclaraciones entrarán en vigencia inmediatamente después de su publicación en el sitio web. Si hacemos cambios materiales a esta política, notificaremos aquí que ha sido actualizada, por lo que cual estás enterado de qué información recopilamos, cómo y bajo qué circunstancias, si las hubiere, la utilizamos y/o divulgamos.

Si nuestra tienda es adquirida o fusionada con otra empresa, tu información puede ser transferida a los nuevos propietarios, para que podamos seguir vendiéndote productos.

Preguntas e información de contacto
Si quieres: acceder, corregir, enmendar o borrar cualquier información personal que poseamos sobre ti, registrar una queja, o simplemente quieres más información contacta a nuestro Oficial de Cumplimiento de Privacidad hey@moonplace.eu        """
    )


if __name__ == "__main__":
    run()
