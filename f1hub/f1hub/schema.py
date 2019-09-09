import graphene

import f1hub.drivers.schema
import f1hub.results.schema
import f1hub.constructors.schema
import f1hub.races.schema
import f1hub.status.schema
import f1hub.circuits.schema
import f1hub.constructorresults.schema
import f1hub.constructorstandings.schema
import f1hub.driverstandings.schema
import f1hub.laptimes.schema
import f1hub.pitstops.schema
import f1hub.qualifying.schema
import f1hub.seasons.schema


class Query(f1hub.drivers.schema.Query, f1hub.results.schema.Query, f1hub.constructors.schema.Query, f1hub.races.schema.Query, f1hub.status.schema.Query, f1hub.circuits.schema.Query,\
    f1hub.constructorresults.schema.Query, f1hub.constructorstandings.schema.Query, f1hub.driverstandings.schema.Query, f1hub.laptimes.schema.Query, f1hub.pitstops.schema.Query,\
    f1hub.qualifying.schema.Query, f1hub.seasons.schema.Query, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
