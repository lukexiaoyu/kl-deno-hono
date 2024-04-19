import {Hono} from "npm:hono"
import { serveStatic } from 'https://deno.land/x/hono/middleware.ts'

const app=new Hono()
app.use('/one/*',serveStatic({root:'./'}))
app.use('/two/*',serveStatic({root:'./'}))

app.get('/',(c)=>c.text('hello'))


Deno.serve(app.fetch)