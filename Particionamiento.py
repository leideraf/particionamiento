""""
Crear Directorios para los Fragmentos
Primero, debemos crear directorios para los datos de los fragmentos.
En este ejemplo, se configurarán tres fragmentos con tres nodos de réplica cada uno.

New-Item -ItemType Directory -Path shard1\data1, shard1\data2, shard1\data3
New-Item -ItemType Directory -Path shard2\data1, shard2\data2, shard2\data3
New-Item -ItemType Directory -Path shard3\data1, shard3\data2, shard3\data3

Iniciar los servidores mongod para los shards

Necesitamos iniciar tres procesos de MongoDB para cada shard
(shard1, shard2, shard3). Cada proceso estará asociado a un puerto y
utilizará una de las carpetas creadas anteriormente.

Para shard1:

mongod --shardsvr --port 26017 --dbpath .\shard1\data1 --replSet shard1_replset
mongod --shardsvr --port 26117 --dbpath .\shard1\data2 --replSet shard1_replset
mongod --shardsvr --port 26217 --dbpath .\shard1\data3 --replSet shard1_replset

Para shard2:

mongod --shardsvr --port 28017 --dbpath .\shard2\data1 --replSet shard2_replset
mongod --shardsvr --port 28117 --dbpath .\shard2\data2 --replSet shard2_replset
mongod --shardsvr --port 28217 --dbpath .\shard2\data3 --replSet shard2_replset

Para shard3:

mongod --shardsvr --port 29017 --dbpath .\shard3\data1 --replSet shard3_replset
mongod --shardsvr --port 29117 --dbpath .\shard3\data2 --replSet shard3_replset
mongod --shardsvr --port 29217 --dbpath .\shard3\data3 --replSet shard3_replset

Configurar los conjuntos de réplica para cada shard
Una vez que los procesos de MongoDB estén ejecutándose, conecta cada conjunto de réplicas
para habilitar la replicación.

Para shard1:
mongosh --port 26017








"""