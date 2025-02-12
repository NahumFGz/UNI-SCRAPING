https://busquedas.elperuano.pe/

Listar todos los resolvers disponibles

```
{
  __schema {
    queryType {
      fields {
        name
        description
      }
    }
  }
}
```

Ver variables de cada resolver

```
query {
  __type(name: "Query") {
    fields {
      name
      args {
        name
        type {
          kind
          name
          ofType {
            kind
            name
          }
        }
      }
    }
  }
}
```

Generar consulta especifica

```
query {
  getNormasPaginated(fechaIni: "20240101", fechaFin: "20240210", start: 0, paginatedBy: 10) {
    totalHits
    hits {
      nombreDispositivo
      sumilla
      urlPDF
      fechaPublicacion
    }
  }
}
```

Otra forma de consultar

```
{
  "fechaIni": "20160101",
  "fechaFin": "20241019",
  "tipoPublicacion": "NL",
  "start": 0
}

```

```
query Generic(
  $fechaIni: String,
  $fechaFin: String,
  $tipoPublicacion: String,
  $start: Int
) {
  results: getGenericPublication(
    fechaIni: $fechaIni
    fechaFin: $fechaFin
    tipoPublicacion: $tipoPublicacion
    start: $start
  ) {
    totalHits
    hits {
      clasificacion1
      clasificacion2
      nombreDispositivo
      op
      paginas
      rubro
      sector
      sumilla
      tipoDispositivo
      urlPDF
      urlPortada
      fechaPublicacion
    }
  }
}

```
