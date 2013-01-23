python-rfc5424-logging-formatter
================================

A Logging Formatter for Python's logging module to properly handle Syslog RFC5424 messages


What is provided by this formatter
----------------------------------

A derived formatter than allows for isotime specification
for full RFC5424 compliancy (with corrected TZ format)

For a "proper" ISOTIME format, use "%(isotime)s" in a
formatter instance of this class or a class derived from
this class.  This is for a work-around where strftime
has no mechanism to produce timezone in the format of
"-08:00" as required by RFC5424.

The '%(isotime)s' replacement will read in the record
timestamp and try and reparse it.  This really is a
problem with RFC5424 and strftime.  I am unsure if this
will be fixed in the future (in one or the other case)

This formatter has an added benefit of allowing for
'%(hostname)s' to be specified which will return a '-'
as specified in RFC5424 if socket.gethostname() returns
bad data (exception).


RFC5424 Format
--------------

RFC: http://tools.ietf.org/html/rfc5424

__The RFC5424 Format should only be used when talking to a Syslog server
over the network stack.  Specifically the Linux KSyslog implementation
still uses RFC3164 format (and something akin to RSyslog still adheres
to that)__

The RFC5424 format string should look somthing like:
```
%(isotime)s %(hostname)s %(name)s %(process)d - - %(message)s
```

The section after the two "- -" is technically the message
section, and can have any data applied to it e.g.:
```
 <...> %(levelname)s [%(module)s %(funcName)s] %(message)s
```

The '- -' section is the "msg ID" and "Structured-Data" Elements,
respectively


Example useage of the formatter
-------------------------------

```python

    import logging

    logger = logging.getLogger('rfc5424_example')
    handler = logging.handlers.SysLogHandler(address=<Address of SysLogServer>)
    format = ''%(isotime)s %(hostname)s %(name)s %(process)d - - %(message)s''
    formatter = RFC5424Syslog(format)

    handler.setFormatter(formatter)

    logger.addHandler(handler)

    logger.info('RFC5424 Log Message Format in use')
```

License
-------

    Copyright (C) 2013 Morgan Fainberg and Metacloud, Inc

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.
