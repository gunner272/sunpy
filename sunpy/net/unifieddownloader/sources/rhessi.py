from sunpy.net.vso.attrs import Time, Instrument
from sunpy.net.unifieddownloader.client import GenericClient
from sunpy.instr import rhessi

__all__ = ['Time', 'Instrument']

class RHESSIClient(GenericClient):
        
	def _get_url_for_timerange(self, timerange, **kwargs):
            """Returns a URL to the RHESSI data for the specified date range.

            Parameters
            ----------
            args : TimeRange, datetimes, date strings
            Date range should be specified using a TimeRange, or start
            and end dates at datetime instances or date strings.
            """
	    if not timerange:
	        return []

            url = rhessi.get_obssum_filename(timerange)
            return [url]


        def _makeimap(self):
	    '''Helper Function:used to hold information about source. '''
	    self.map_['source'] = ''
	    self.map_['instrument'] = 'rhessi'
	    self.map_['phyobs'] = 'irradiance'
	    self.map_['provider'] = 'nasa'
        
        @classmethod
        def _can_handle_query(cls, *query):
            """Boolean Function:Answers whether client can service the query.
            """
	    chkattr =  ['Time', 'Instrument']
            chklist =  [x.__class__.__name__ in chkattr for x in query]
            for x in query:
	        if x.__class__.__name__ == 'Instrument' and x.value == 'rhessi':
                    return all(chklist)
	    return False
 

