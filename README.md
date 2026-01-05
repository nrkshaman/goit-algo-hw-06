## Graph analysis(Taks 1)
- Number of nodes: 15
- Number of edges: 20
- Is cconnected: True
- Degree centrality:
```javascript 
{
'Acciaiuoli': 0.07142857142857142, 
'Medici': 0.42857142857142855, 
'Castellani': 0.21428571428571427, 
'Peruzzi': 0.21428571428571427, 
'Strozzi': 0.2857142857142857, 
'Barbadori': 0.14285714285714285, 
'Ridolfi': 0.21428571428571427, 
'Tornabuoni': 0.21428571428571427, 
'Albizzi': 0.21428571428571427, 
'Salviati': 0.14285714285714285, 
'Pazzi': 0.07142857142857142, 
'Bischeri': 0.21428571428571427, 
'Guadagni': 0.2857142857142857, 
'Ginori': 0.07142857142857142, 
'Lamberteschi': 0.07142857142857142
}
```
## Traversal analysis(Taks 2)
### BFS route:
1. Lamberteschi 
2. Guadagni
3. Tornabuoni
4. Albizzi
5. Bischeri
6. Medici
7. Ridolfi
8. Ginori
9. Peruzzi
10. Strozzi
11. Barbadori
12. Salviati
13. Acciaiuoli
14. Castellani
15. Pazzi

### DFS route:
1. Lamberteschi
2. Guadagni
3. Tornabuoni
4. Medici
5. Acciaiuoli
6. Barbadori
7. Castellani
8. Peruzzi
9. Strozzi
10. Ridolfi
11. Bischeri
12. Albizzi
13. Ginori
14. Salviati
15. Pazzi 

### Conclusion
As expected from the Breadth First Algorithm, it took this route because it prioritizes going wide. It means that this algorithm will visit all immediate neighbors of the current node before going to the next node. Contrary to BFS, the Depth First Algorithm prioritizes going deep. It does this by going to the next node on the first opportunity and coming back when it reaches a dead end.