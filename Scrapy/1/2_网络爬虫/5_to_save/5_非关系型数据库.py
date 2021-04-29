非关系型数据库
    1:NoSQL, Not only SQL, 泛指非关系型数据库, NoSQL 基于键值对的,而且不需要经过 SQL 层
      的解析, 数据之间没有耦合性,性能非常高
    2:非关系型数据库分类
        键值存储数据库: 代表有 Redis, Voldemort, Oracle BDB
        列存储数据库: 代表有 Cassandra, HBase, Riak
        文档型数据库: 代表有 CouchDB, MongoDB
        图形数据库: 代表有 Neo4J, InfoGrid, Infinite Graph 等
    3:对于爬虫的数据来说,一条数据可能存在某些字段提取失败而缺失的情况,而且数据可能随时调整.
      另外,数据之间还存在嵌套关系.如果使用关系型数据库存储, 一是需要提前建表,二是如果存在数据
      嵌套关系的话,需要进行序列化操作才可以存储.这非常不方便.如果用了非关系型数据库,就可以避免
      一些麻烦更简单高效.
