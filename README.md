# Mitschrieb zur Vorlesung Algorithmen für planare Graphen am KIT im Sommersemester 2015

Der Mitschrieb wurde von mir während der Vorlesungen erstellt. Er sollte alles enthalten was Frau Prof. Wagner an die Tafel geschrieben hat.

## Bekannte Probleme

* Die meisten Bilder fehlen. Da wo Graphen sind ist aktuell einfach *(todo: Bild)* o.ä.
* Überschriftenebenen sind teilweise vielleicht nicht richtig, weil das in der Vorlesung nicht immer auf den ersten Blick erkenntlich war.

Falls da jemand was fixen will nehme ich natürlich gerne Pull-Requests ;)

## Bauen

Das PDF ist mit im Repo drin.

Es wird erstellt mithilfe von [pandoc](pandoc.org/README.html) aus den Markdown-Dateien via lualatex.

Beispiel zur Einrichtung:

```bash
# arch:
sudo pacaur -S pandoc-bin
# debian:
sudo apt-get install pandoc


sudo pip2 install pandocfilters pygraphviz

make
```
