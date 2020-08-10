# InlineResponse2002KeyInformation

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** | Merchant Id  | [optional] 
**reference_number** | **str** | Reference number is a unique identifier provided by the client along with the organization Id. This is an optional field provided solely for the client’s convenience. If client specifies value for this field in the request, it is expected to be available in the response.  | [optional] 
**key_id** | **str** | Key Serial Number  | [optional] 
**status** | **str** | The status of the key.  Possible values:  - FAILED  - ACTIVE  - INACTIVE  - EXPIRED  | [optional] 
**expiration_date** | **str** | The expiration time in UTC. &#x60;Format: YYYY-MM-DDThh:mm:ssZ&#x60;  Example 2016-08-11T22:47:57Z equals August 11, 2016, at 22:47:57 (10:47:57 p.m.). The T separates the date and the time. The Z indicates UTC.  | [optional] 
**message** | **str** | message in case of failed key | [optional] 
**alias** | **str** | Key alias | [optional] 
**error_information** | [**InlineResponse201ErrorInformation**](InlineResponse201ErrorInformation.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


