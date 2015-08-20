# Algorithmen für planare Graphen

## Einführung

ungerichteter, einfacher Graph G = (V,E)
Einbettung (in die Ebene):

'K2,3 + weitere Graphen'

- Kooridinaten für Knoten, Kanten als Geraden bzw. Kurven -> geometrische Einbettung
- Anordnung der Kanten in Adjazenzliste -> kombinatorische Einbettung

Ein Graph, der sich kreuzungsfrei  in die Ebene einbetten lässt ist planar.
Bsp: 'Graphen'

### $K_5$ ist nicht planar, denn:
angenommen es gäbe planare Einbettung von $K_5$, o.B.d.A. mit Knoten 1 kreuzungsfrei zu Knoten 2,3,4 und 5 verbunden, im Uhrzeigersinn. Einbettung der Kante {2,4} zerlegt Ebene in zwei Gebiete:
"Inneres" von 1241 und "Äußeres" von 1241
⇒ Kante {3,5} muss dann Kante {2,4} kreuzen
'Illustration'

### $K_{3,3}$ ist nicht planar, denn:
$K_{3,3}$ = (V,E), V := {1,2,3,g,w,s}, E := {{i,j}: i $\in$ {1,2,3}, j $\in$ {g,w,s}}
angenommen $K_{3,3} besitze kreuzungsfreie Einbettung, o.B.d.A. mit Kreis w1g2s3w kreuzungsfrei mit {1,s} im Inneren des Kreises
⇒ {2,w} im Äußeren.
Dann ist {3,g} nicht mehr kreuzungsfrei einbettbar.

Graphen, die K5 oder K3,3 "enthalten" können also nicht planar sein.

### Im Folgenden:
- Charakterisierung planarer Graphen "Satz von Kuratowski"
- Planaritätstest geht in Linearzeit
- es gibt Probleme, die i.A. NP-schwer sind, und in planaren Graphen polynomial lösbar, z.B. Max-Cut
- polynomial lösbare Probleme, die in pl. Graphen effizieneter (oft in Linearzeit) gelöst werden können, z.B. Matchings, Menger, MaxFlow ...

### Vierfarbensatz:
Jede Landkarte kann mit 4 Farben gefärbt werden. "Dualgraph" zu Landkarte ist planarer Graph (Länder als Knoten, Kanten als Grenzen) -> jder pl. Graph kann mit 4 Farben gefärbt werden


#### Einschub: Konzept des Dualgraphen
planarer Graph G = (V,E) mit pl. Einbettung mit Facettenmenge F von G bzgl. dieser Einbettung.
Definiere dazu Dualgraph G* = (V*,E*) wie folgt:
- zu jeder Facette f $\in$ F def. Knoten $v_f$ in V*
- zu jeder Kante e = {u,v} $\in$ E gibt es eine Kante e* $\in$ E*, die die beiden Knoten in V* zu den Facetten in F, die durch e getrennt werden, verbindet. 
G = (V,E), F = ${f_1,f_2,f_3}$ 'Graph mit Dualgraph'
G = (V,E), andere Darstellung 'Graph'

Eigenschaften des Dualgraphen:
i) Dualgraph G* zu einfachem planaren Graphen ist i.A. nicht einfach
ii) Dualgraph G* ist wieder planar und (G*)* = G (wobei G* Dualgraph zu G)
iii) planarer Graph G kann verschiedene Dualgraphen haben (zu verschiedenen Einbettungen)


### Satz (1977 Appel & Haken)
Jeder pl. Graph kann mit höchstens 4 Farben gefärbt werden.
Beweis mit Fallunterscheidung.

#### "Folklore": 
pl. Graph kann mit 5 Farben gefärbt werden.
Beweis per Induktion über Anz. Knoten n.
IS: G habe n Knoten, v sei Knoten in G mit min. Grad.
Dann ist d(v) <= 5 (Beweis später)
Entscheidender Fall: d(v) = 5:
sei Facette von v so eingebettet:
'Bild'
Dann ex. gegenüberliegende Knoten i,j \in {1,2,3,4,5} mit {i,j} $\notin$ E.
Verschmelze i und j und färbe nach IV entspr. Graph mit 5 Farben. Dies induziert 5-Färbung von G-v, in der i und j dieselbe Farbe haben und entsprechend {1,2,3,4,5} nur 4 Farben benutzen. ⇒ Beh.
'Bild'
