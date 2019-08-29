# Progetto finale per il corso di Information Visualization

## Demo

La demo è in formato gif, è possibile anche scaricarla in formato mp4 

![](demo.gif)

## Ambiente di esecuzione 

Questa applicazione può eseguita in un ambiente in cui vi siano installati:

* Docker 

* Docker compose 

## Docker Settings

Settings minimi: 2 CPUs, 4 GB RAM <br/>
Settings consigliati: 4 CPUs, 8 GB RAM <br/>
Spazio richiesto: 5-6 GB

## Abilitare popup e reindirizzamenti

Per il corretto funzionamento dell'applicazione è necessario abilitare i popup e reindirizzamenti dal proprio browser.<br/>
Chrome: impostazioni -> Avanzate -> Privacy e sicurezza -> Impostazioni sito -> Popup e reindirizzamenti -> spuntare su Consentito

## Esecuzione 

Lo script di avvio è impostato per aprire la pagina html da google-chrome con un comando windows. <br/>
Per eseguire l'applicazione, aprire un terminale, spostarsi nella cartella del progetto ed eseguire lo script <br/>
`run-application.sh.`
Tempo richiesto per la costruzione delle immagini Docker (solo primo avvio): circa 5 minuti <br/>
Tempo richiesto l'avvio dell'applicazione (con immagini già costruite): circa 2 minuti

## Arresto 

Per arrestare l'applicazione, aprire un altro terminale ed eseguire lo script `stop-application.sh`
