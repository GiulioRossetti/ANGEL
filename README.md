# ANGEL

Community discovery in complex networks is an interesting problem with a number of applications, especially in the knowledge extraction task in social and information networks. However, many large networks often lack a particular community organization at a global level. In these cases, traditional graph partitioning algorithms fail to let the latent knowledge embedded in modular structure emerge, because they impose a top-down global view of a network. We propose here a simple local-first approach to community discovery, able to unveil the modular organization of real complex networks. This is achieved by democratically letting each node vote for the communities it sees surrounding it in its limited view of the global system, i.e. its ego neighborhood, using a label propagation algorithm; finally, the local communities are merged into a global collection. 

## Citation
If you use our algorithm please cite the following works:


## Implementation details

Required input format: .ncol edgelist (nodes represented with integer ids).

```
node_id0    node_id1
```

# Execution
Angel is written in python and requires the following package to run:
- python 2.7.10
- igraph/networkx
- tqdm

The algorithm can be used as standalone program as well as integrated in python scripts.

Both an igraph (iAngel.py) and a networkx (Angel.py) implementations are provided.

## Standalone

```bash

python Angel.py filename epsilon -c min_com_size -o out_filename 
```

where:
* filename: edgelist filename
* epsilon: merging threshold in [0,1]
* min_com_size: minimum size for communities (default 3 - optional)
* out_filename: desired filename for the output (optional)

The explicit removal version does not expose the ttl parameter.

## As python library

```python
import Angel as a
an = t.Angel("filename.ncol", epsilon=0.25, min_com_size=3, out_filename="communities.txt")
an.execute()
```
