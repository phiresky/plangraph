> 2015-06-17

## Zu Phase 2

Sei von Startterminal im Gegenuhrzeigersinn jeweils $s_i$ vor $t_i$ und Indizierung entsprechend Auftreten der ti.

> Für i = 1 bis k
>
> > RFS von $s_i$ aus bis zu einem $t_j$ \} $\leadsto p_i$
> > 
> > falls $j\neq t$ stop
>
> gib $p_1,\dots,p_k$ aus

#### Laufzeit

$O(n)$ amortisiert mit UNION-FIND wie kantendisj. Menger

#### Korrektheit

Algorithmus findet entweder

i) mit Wegen $p_i\dots p_k$ die jeweils $s_i$ mit $t_i$ verbinden oder
ii) $p_1,\dots,p_{i-1}$ "korrekt" und $p_i$ verbindet $s_i$ mit $t_j,i\neq j\implies i<j$

$\leadsto$ Prozedur, die Weg p berechnet, so dass p einen Schnitt X induziert, der

- im Fall i) "saturiert" ist, d.h. $fcap(X)=0$
- im Fall ii) "übersaturiert" ist, d.h. $fcap(X)<0$

⇒ Korrektheit

Prozedur für Schritt X:

Rückwärts-LFS startend von Terminal $t_i$ bzw. $t_j$ wo Weg $p_i$ endet in Graph, der durch $p_1\dots p_i$ induziert wird.

#### Lemma

Sei A Menge der Kanten $\{u,v\}$ aus G mit u auf p und v rechts von p. Jede Kante $\{u,v\} \in A$ gehört zu $\vec{G}$ und genau dann in Orientierung $(u,v)$ wenn sie durch einen der $p_1\dots p_i$ besetzt ist.

#### Beweis

Wenn $\{u,v\}$ durch ein $p_i$ besetzt, dann wegen Konstruktion von p in Orientierung $(u,v)$.

*Fall 1*: es existiere $(u,v)$ mit $(u,v)$ *nicht* durch $p_1\dots p_i$ besetzt.
`bild` Widerspruch zu RFS in Phase 2

*Fall 2*: es existiert $\{u,v\}\in A, (u,v), (v,u) \notin \vec{G}$ ⇒ Widerspruch zu RFS in Phase 1

#### Lemma

Sei X Schnitt induziert durch p (Knoten rechts von p). Falls $p_i$ $s_i-t_i-Weg$, so ist $fcap(X)=0$ ansonsten $fcap(X)<0$.

#### Beweis

Kanten $\{u,v\}$ auf p, v rechts von p entweder zu Weg $p_j$ gehört mit $1\leq j\leq i, s_j\in  V\setminus X \text{ und } t_j \in X$ oder zu Weg $q_j$ aus erster Phase mit $s_j'\in X$ und $t_j' \in V \setminus X$.

Wenn $p_i$ korrekter $s_i-t_i-$Weg so gibt
$$cap(X) = |\{\{s_j,t_j\}:s_j\in V\setminus X, t_j \in X, 1\leq j \leq i\}|+|\{\{s_j',t_j'\}: s_j'\in X $$$$\text { und } t_j' \in V\setminus X, \{s_i',t_j'\}\notin \{\{s_1,t_1\},\dots\{s_{i-1},t_{i-1}\}\}| = dens(X)$$

Wenn $p_i$ nicht korrekt, d.h. $s_i$ mit $t_j, i<j$ verbindet, so ist $cap(X)<dens(X)$, da $s_i\in V\setminus X, t_i \in X$.
