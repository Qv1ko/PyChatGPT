import openai,typer
from rich import print
from rich.table import Table

def main():

    #ChatGPT API key
    openai.api_key="tu_api_key"

    print("🤖 [bold green]ChatGPT API en Python[/bold green]")

    #Tabla de guía de comandos
    table=Table("Comando","Descripción")
    table.add_row("exit","Salir de la aplicación")
    table.add_row("new","Crear una nueva conversación")
    print(table)

    #Contexto del asistente
    context={"role":"system","content":"Eres un asistente muy útil."}
    messages=[context]

    while True:

        content=__prompt()

        #Condicional de nueva conversación
        if content=="new":
            print("\n🆕 [blue]Nueva conversación iniciada[/blue]")
            messages=[context]
            content=__prompt()

        #Respuesta de ChatGPT
        messages.append({"role":"user","content":content})
        response=openai.ChatCompletion().create(model="gpt-3.5-turbo",messages=messages)
        response_content=response.choices[0].message.content
        messages.append({"role":"assistant","content":response_content})

        print(f"\n[bold green]> [/bold green][green]{response_content}[green]")

def __prompt() -> str:

    prompt=typer.prompt("\n👱 Mensaje ")

    #Condicional de salida
    if prompt=="exit":
        exit=typer.confirm("\n⚠ ¿Estas seguro?")
        if exit:
            print("\n👋 Saliendo...")
            raise typer.Abort()
        return __prompt()

    return prompt

if __name__=="__main__":
    typer.run(main)