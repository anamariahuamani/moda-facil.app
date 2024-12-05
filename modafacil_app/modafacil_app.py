import reflex as rx


def index()->rx.Component:
  return rx.flex(
      rx.hstack(
        rx.vstack(
            #rx.card(rx.button(rx.icon(tag="store",color="#3d1d0b")),size="5"),
            rx.link(
              rx.card(
                rx.icon(tag="store",color="#3d1d0b"),
                size="5"
              ),
              href="/vendedor" ,
            ),
            rx.heading("Vendedor",color="#DDA0DD"),      
        ),
        rx.vstack(
           rx.link(
             rx.card(
               rx.icon(tag="shopping-carritos",color="#3d1d0b"),
               size="4"
             ),
             href="/usuario" ,
           ),
           rx.heading("usuari",color="#D2B48C"),
            # rx.card(rx.icon(tag="shopping-carrito",color="#B784A7"),size="5"),
            # rx.heading("usuario",color="#3d1d0b"),      
        ),
      ),
    align="center",
    justify="center",
    background="#F7BFBE",
    height="100vh"
  )
  
  
app=rx.App()
app.add_page(index)

  
        